"""Database models for the ``orders`` application.

The project did not previously define any order related models.  For the
tests to interact with orders we introduce two small models – ``Order`` and
``OrderItem`` – which capture basic customer and payment information.  The
models intentionally keep the fields lightweight so they can be reused in
multiple contexts without pulling in a fully‑fledged e‑commerce system.
"""

from django.db import models


class Order(models.Model):
    """Represents a customer's order.

    Stores the customer's contact details, the total amount paid for the
    order and identifiers returned from Stripe.  ``created_at`` and
    ``updated_at`` are included to make the model easier to inspect and sort
    in the admin interface.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    total = models.DecimalField(max_digits=10, decimal_places=2)

    # Stripe identifiers used to reconcile payments
    stripe_payment_intent = models.CharField(
        max_length=255, blank=True, null=True
    )
    stripe_checkout_session = models.CharField(
        max_length=255, blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"Order #{self.pk}"


class OrderItem(models.Model):
    """A single line item within an :class:`Order`."""

    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE
    )
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"{self.product_name} ({self.quantity})"

    @property
    def total_price(self):
        """Return the total price for this line item."""
        return self.price * self.quantity

