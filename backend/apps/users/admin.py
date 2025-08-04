"""Admin registrations for user related models."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Admin configuration for the custom ``User`` model."""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Info",
            {"fields": ("phone_number", "address")},
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("phone_number", "address")}),
    )
    list_display = ("username", "email", "phone_number", "is_staff")
    search_fields = ("username", "email", "phone_number")

