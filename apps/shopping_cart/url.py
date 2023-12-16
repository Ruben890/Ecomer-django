from django.urls import path
from .views import ShoppingCart, DeleteProductCard, ShoppingViews
urlpatterns = [
    path('', ShoppingCart.as_view(),  name='shopping_cart'),
    path('delete/<int:id>/', DeleteProductCard.as_view(), name='delete_product'),
    path('shopping_cart/',ShoppingViews.as_view(), name='shopping_cart' )
]