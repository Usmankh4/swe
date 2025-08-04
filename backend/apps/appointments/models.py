"""Models related to booking repair appointments."""

from django.db import models
from apps.repairs.models import RepairPrice


class Appointment(models.Model):
    """An appointment booked by a customer for a repair."""

    repair_price = models.ForeignKey(
        RepairPrice, related_name="appointments", on_delete=models.CASCADE
    )
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    scheduled_for = models.DateTimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["scheduled_for"]

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"{self.customer_name} @ {self.scheduled_for:%Y-%m-%d %H:%M}"
