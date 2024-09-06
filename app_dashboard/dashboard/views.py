from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import App, Plan, Subscription
from .serializers import (
    AppSerializer,
    PlanSerializer,
    SubscriptionSerializer,
    SubscriptionUpdateSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User

# Register View
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allow any user (authenticated or not) to access this view

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')

        if not username or not password:
            return Response(
                {'error': 'Username and password are required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'Username already exists.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(
            {'message': 'User created successfully.'},
            status=status.HTTP_201_CREATED,
        )

class AppViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically associate the Free Plan upon app creation
        app = serializer.save(user=self.request.user)
        free_plan = Plan.objects.get(name="Free")
        Subscription.objects.create(app=app, plan=free_plan)

    def get_queryset(self):
        # Return only apps owned by the authenticated user
        return App.objects.filter(user=self.request.user)

# Plan ViewSet (read-only)
class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]

# Subscription ViewSet
class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only subscriptions for the authenticated user's apps
        return Subscription.objects.filter(app__user=self.request.user)

    def update(self, request, *args, **kwargs):
        subscription = self.get_object()
        plan_id = request.data.get('plan')
        try:
            new_plan = Plan.objects.get(id=plan_id)
        except Plan.DoesNotExist:
            return Response(
                {"error": "Plan not found."}, status=status.HTTP_404_NOT_FOUND
            )

        subscription.plan = new_plan
        subscription.save()
        return Response(
            {'message': 'Subscription updated successfully.'},
            status=status.HTTP_200_OK,
        )

    def perform_destroy(self, instance):
        # Instead of deleting the subscription, deactivate it
        instance.active = False
        instance.save()
        return Response({'message': 'Subscription deactivated.'}, status=status.HTTP_200_OK)
