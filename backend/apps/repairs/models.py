"""Database models for the ``repairs`` application.

These simple models store the different types of repairs offered by the
business and the price for each repair depending on the device.  They are
intentionally lightweight so that other parts of the project – such as the
``appointments`` app – can reference them without pulling in extra
complexity.
"""

from django.db import models


class RepairType(models.Model):
    """A category of repair, e.g. screen replacement or battery change."""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return self.name


class RepairPrice(models.Model):
    """Price information for a given repair and device."""

    repair_type = models.ForeignKey(
        RepairType, related_name="prices", on_delete=models.CASCADE
    )
    device_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"{self.device_name} - {self.repair_type.name}"
