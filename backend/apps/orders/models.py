from django.conf import settings
from django.db import models


class Order(models.Model):
    """Represents a purchase made by a user.

    The Stripe payment intent ID is stored to allow the backend to
    reconcile payments made through the checkout flow.
    """

    STATUS_PENDING = "pending"
    STATUS_PAID = "paid"
    STATUS_FAILED = "failed"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_PAID, "Paid"),
        (STATUS_FAILED, "Failed"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    stripe_payment_intent = models.CharField(max_length=255, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"Order #{self.pk} by {self.user}"


class OrderItem(models.Model):
    """Individual item within an order.

    This model is intentionally generic – items may correspond to products,
    repair services or other purchasable entities.  The description and
    price fields capture the state at the time of purchase.
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
    )
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"{self.quantity} x {self.description}"
