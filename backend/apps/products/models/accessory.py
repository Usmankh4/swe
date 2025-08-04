from django.db import models
from .abstract_product import AbstractProduct
from .brand import Brand

class Accessory(AbstractProduct):
    
    ACCESSORY_TYPES = [
        ('case', 'Phone Case'),
        ('screen_protector', 'Screen Protector'),
        ('charger', 'Charger'),
        ('headphones', 'Headphones'),
        ('other', 'Other'),
    ]
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='accessories')
    accessory_type = models.CharField(max_length=50, choices=ACCESSORY_TYPES)
    compatible_with = models.ManyToManyField('Phone', related_name='compatible_accessories', blank=True)
    
    class Meta:
        verbose_name_plural = 'Accessories'
        ordering = ['accessory_type', 'brand__name', 'name']
    
    def __str__(self):
        return f"{self.brand.name} {self.name} ({self.get_accessory_type_display()})"
