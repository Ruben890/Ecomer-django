from django.contrib import admin
from .models import Product, ProductImage, Rating, Type, Category

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Rating)
admin.site.register(Type)
admin.site.register(Category)