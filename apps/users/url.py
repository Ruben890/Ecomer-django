from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
     # ? Auth AUTHENTICATION
    path('login', CustomLoginView.as_view(), name="login"),
    path('register', CreateUsersView.as_view(), name="register"),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
]