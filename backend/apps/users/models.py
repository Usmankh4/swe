from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    """Additional information associated with a user account."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    stripe_customer_id = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:  # pragma: no cover - simple representation
        return f"Profile for {self.user}"
