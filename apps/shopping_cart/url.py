from django.urls import path
from .views import ShoppingCart, DeleteProductCard, ShoppingViews, UpdateQuantity
urlpatterns = [
    path('', ShoppingCart.as_view(),  name='shopping_cart'),
    path('delete/<int:id>/', DeleteProductCard.as_view(), name='delete_product'),
    path('shopping_cart/', ShoppingViews.as_view(), name='shopping_cart'),
    path('update_quantity/<int:id>/', UpdateQuantity.as_view(), name='update_quantity'),
]