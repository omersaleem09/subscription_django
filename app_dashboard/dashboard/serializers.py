from rest_framework import serializers
from .models import App, Plan, Subscription

# App Serializer
class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'name', 'description']

# Plan Serializer
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'price', 'description']

# Subscription Serializer
class SubscriptionSerializer(serializers.ModelSerializer):
    app = AppSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'app', 'plan', 'active', 'subscribed_at']

# Subscription Update Serializer (for updating plan)
class SubscriptionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['plan']
