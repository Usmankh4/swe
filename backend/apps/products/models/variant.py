from django.db import models

from .phone import Phone


class PhoneVariant(models.Model):
    """Represents a specific variant of a phone model."""

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
        ordering = ["phone", "variant_name"]

    def __str__(self) -> str:
        return f"{self.phone} - {self.variant_name}"

