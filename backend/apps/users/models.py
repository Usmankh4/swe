"""User models for the project."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model extending Django's ``AbstractUser``.

    The default ``User`` model provided by Django is extended with a couple of
    optional fields that are useful for an eCommerce oriented application.  The
    model remains fully compatible with Django's authentication system and can
    be referenced via ``settings.AUTH_USER_MODEL``.
    """

    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.get_username()

