"""Models related to repair services and pricing."""

from django.db import models


class RepairService(models.Model):
    """A type of repair that can be performed on a device."""

    device_name = models.CharField(max_length=100)
    issue = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("device_name", "issue")
        ordering = ["device_name", "issue"]

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"{self.device_name} - {self.issue}"

