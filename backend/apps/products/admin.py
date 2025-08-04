from django.contrib import admin

from .models.brand import Brand
from .models.phone import Phone
from .models.variant import PhoneVariant
from .models.accessory import Accessory


admin.site.register(Brand)
admin.site.register(Phone)
admin.site.register(PhoneVariant)
admin.site.register(Accessory)

