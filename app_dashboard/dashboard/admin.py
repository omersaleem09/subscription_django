from django.contrib import admin

# Register your models here.
from .models import App, Plan, Subscription

admin.site.register(App)
admin.site.register(Plan)
admin.site.register(Subscription)