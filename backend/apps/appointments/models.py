"""Models for scheduling appointments."""

from django.conf import settings
from django.db import models


class Appointment(models.Model):
    """Represents a scheduled meeting with a customer."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    scheduled_for = models.DateTimeField()
    notes = models.TextField(blank=True)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-scheduled_for"]

    def __str__(self) -> str:  # pragma: no cover - trivial
        return f"Appointment {self.pk}"

