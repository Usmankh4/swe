from django.db import models


class RepairPrice(models.Model):
    """Defines the cost of a particular repair.

    A combination of ``device_type`` and ``repair_type`` should be unique so
    that each repair service can be referenced consistently from other parts
    of the application.
    """

    device_type = models.CharField(max_length=100)
    repair_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ("device_type", "repair_type")
        ordering = ["device_type", "repair_type"]

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"{self.device_type} {self.repair_type} - {self.price}"
