"""Admin registrations for repair models."""

from django.contrib import admin

from .models import Repair


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "device", "status", "created_at")
    list_filter = ("status", "created_at")

