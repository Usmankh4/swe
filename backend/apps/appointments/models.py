"""Database models for managing repair appointments."""

from django.conf import settings
from django.db import models


class Appointment(models.Model):
    """Represents a scheduled repair appointment for a user."""

    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (CONFIRMED, "Confirmed"),
        (COMPLETED, "Completed"),
        (CANCELLED, "Cancelled"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    repair_service = models.ForeignKey(
        "repairs.RepairService",
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    scheduled_time = models.DateTimeField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=PENDING
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-scheduled_time"]

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"Appointment for {self.user} at {self.scheduled_time}"

