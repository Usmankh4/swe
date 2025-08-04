"""Model for individual variants of a phone model.

For example, a phone might come in different storage capacities or colors.
"""

from django.db import models

from .phone import Phone


class PhoneVariant(models.Model):
    """A specific variant of a :class:`Phone`."""

    phone = models.ForeignKey(
        Phone,
        on_delete=models.CASCADE,
        related_name="variants",
    )
    variant_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["phone__name", "variant_name"]

    def __str__(self) -> str:  # pragma: no cover - trivial string repr
        return f"{self.phone.name} - {self.variant_name}"


__all__ = ["PhoneVariant"]