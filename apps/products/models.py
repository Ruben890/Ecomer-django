import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.conf import settings

# class Currency(models.Model):
#     name = models.CharField(max_length=50, null=False, blank=False)

#     def __str__(self):
#         return self.name

class ProductImage(models.Model):
    image = models.ImageField(upload_to="media/img", verbose_name="imagen adicional")

class Type(models.Model):
    type = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.type

class Category(models.Model):
    category_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="categoría")
    types = models.ManyToManyField(Type, related_name='categories', verbose_name="tipos de producto")

    def __str__(self):
        return self.category_name


class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="nombre del producto", unique=True)
    model = models.CharField(max_length=100, null=False, blank=False, verbose_name="modelo del producto", unique=True)
    price = models.IntegerField(null=False, blank=False, verbose_name="precio del producto")
    images = models.ManyToManyField(ProductImage, related_name='products', verbose_name="imágenes del producto")
    description = models.TextField(max_length=500, null=False, blank=False, verbose_name="descripción del producto")
    video = models.FileField(upload_to="media/videos", null=True, blank=True, verbose_name="video del producto")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="categoría del producto")
    types = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='products', verbose_name="tipo de producto")
    brand = models.CharField(max_length=100, null=False, blank=False, verbose_name="Marca del producto")

    def __str__(self):
        return f'{self.uuid}-{self.name}'

    def calcular_puntuacion_promedio(self):
        ratings = self.ratings.all()
        if not ratings:
            return 0
        total_score = sum(rating.score for rating in ratings)
        average_score = total_score / len(ratings)
        return round(average_score, 2)

@receiver(pre_save, sender=Product)
def generate_uuid(sender, instance, **kwargs):
    if not instance.uuid:
        instance.uuid = uuid.uuid4()


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="usuario")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings', verbose_name="producto")
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="puntuación")

    def __str__(self):
        return f'{self.user.username} - {self.product.name}: {self.score}'

    class Meta:
        unique_together = ('user', 'product')
