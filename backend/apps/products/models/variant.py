from django.db.models.fields import related



class PhoneVariant(models.Model):
    phone = models.ForeignKey(
        Phone,
        on_delete=models.CASCADE,
        related_name='variants'
    )
    variant_name = model.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.phone.name} - {self.variant_name}"