from django.db import models

class Brand(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
   
   
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
