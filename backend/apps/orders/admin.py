"""Admin configuration for the ``orders`` application."""

from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "total",
        "stripe_payment_intent",
        "created_at",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "stripe_payment_intent",
        "stripe_checkout_session",
    )
    list_filter = ("created_at",)
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product_name", "price", "quantity")
    search_fields = ("product_name",)
