from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text= 'Brand name e.g. Apple or Samsung')
    slug= models.SlugField(max_length=100, unique=True, help_text='URL friendly version of the name, e.g., apple')
    created_at = models.DateField(auto_now_add=True, help_text='The date and time of the brand was created')
    def __str__(self):
        return self.name
