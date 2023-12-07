from django.db import models
from django.conf import settings
from apps.products.models import Product

class CarritoItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="user")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="product")
    cantidad = models.PositiveIntegerField(default=1, verbose_name="quantity")

    def __str__(self):
        return f'{self.user.email} - {self.product.name} - {self.cantidad}'
    
