"""Admin registrations for appointment models."""

from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "scheduled_for", "is_confirmed")
    list_filter = ("is_confirmed", "scheduled_for")

