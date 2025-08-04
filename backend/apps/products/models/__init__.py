"""Model declarations for the products app.

This module exposes the concrete product models so that Django's automatic
model discovery (which imports ``<app>.models``) picks them up when the app is
loaded. By importing the models here, we ensure that they are registered with
the app registry.
"""

from .brand import Brand
from .phone import Phone
from .variant import PhoneVariant
from .accessory import Accessory

__all__ = [
    "Brand",
    "Phone",
    "PhoneVariant",
    "Accessory",
]
