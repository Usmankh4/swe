from django.conf import settings
from django.db import models

from apps.repairs.models import RepairPrice


class Appointment(models.Model):
    """A booking for a repair service."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    repair = models.ForeignKey(
        RepairPrice,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    scheduled_for = models.DateTimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-scheduled_for"]

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"{self.user} - {self.repair} on {self.scheduled_for:%Y-%m-%d %H:%M}"
