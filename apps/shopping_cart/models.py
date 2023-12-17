from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from apps.products.models import Product

class ShoppingCartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="user")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="product")
    quantity = models.PositiveIntegerField(default=1, verbose_name="quantity")

    def __str__(self):
        return f'{self.user.email} - {self.product.name} - {self.quantity}'

    def clean(self):
        if not (0 <= self.quantity <= 100):
            raise ValidationError({'quantity': 'Quantity must be between 0 and 100.'})
