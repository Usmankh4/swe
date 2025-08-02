from django.db import models
from .abstract_product import AbstractProduct
from .brand import Brand

class Phone(AbstractProduct):
    
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='phones')
    model = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    operating_system = models.CharField(max_length=50)
    screen_size = models.DecimalField(max_digits=3, decimal_places=1)  # in inches
    storage_capacity = models.PositiveIntegerField(help_text="Storage in GB")
    ram = models.PositiveIntegerField(help_text="RAM in GB")
    
    class Meta(AbstractProduct.Meta):
        ordering = ['-release_year', 'brand__name', 'model']
    
    def __str__(self):
        return f"{self.brand.name} {self.model}"
