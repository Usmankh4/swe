"""Aggregate product models for Django's auto-discovery."""

from .models.brand import Brand
from .models.phone import Phone
from .models.variant import PhoneVariant
from .models.accessory import Accessory

__all__ = ["Brand", "Phone", "PhoneVariant", "Accessory"]

