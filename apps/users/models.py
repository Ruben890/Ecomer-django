from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .choices import GENDER_CHOICES, ROLES_CHOICES
from django.utils.translation import gettext_lazy as _


from .managers import CustomAccountManager


class Profiles(AbstractBaseUser ,PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    Tel = models.CharField(max_length=15, blank=True, null=True, unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15, blank=True, null=True)
    roles = models.PositiveSmallIntegerField(choices=ROLES_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=150, blank=False, null=False)
    address = models.CharField(max_length=250, blank=False, null=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}-({self.email})'

    def has_perm(self, perm, obj=None):
        if self.is_staff:
            return True
        
    def has_module_perms(self, app_label):
        return self.is_staff
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


