from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
urlpatterns = [
    path('search_results', SearchResults.as_view(), name='search_results' ),
    path('detailtProduc/<str:uuid>', detailtProduct.as_view(), name="detailtProduct")


]