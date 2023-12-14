from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.products.views import HomePage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePage.as_view(), name='home'),
    path("product/", include('apps.products.url'), name='product'),
    path('shopping_cart/', include('apps.shopping_cart.url')),
    path("__reload__/", include("django_browser_reload.urls")),  # Django-tailwind
    path('accounts/', include('allauth.urls')), # auth social
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
