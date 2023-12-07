from django import forms
from .models import Profiles
from .choices import GENDER_CHOICES, ROLES_CHOICES
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Password'})
    )

class CreateUsersForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['email', 'first_name', 'last_name', 'image', 'DNI','Tel', 'gender', 'roles', 'country', 'address']

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Email'})
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Password'})
    )

    Confirm_Password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Confirm Password'})
    )
    first_name = forms.CharField(
        max_length=100,  widget=forms.TextInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Last Name'})
    )
    image = forms.ImageField(
        required=False, widget=forms.FileInput(attrs={'class': 'border p-2 w-full'})
    )
    Tel = forms.CharField(
        max_length=10, widget=forms.TextInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Phone', 'type': 'tel'})
    )
    gender = forms.CharField(
        widget=forms.Select(choices=GENDER_CHOICES, attrs={'class': 'border p-2 w-full'})
    )

    roles = forms.IntegerField(
        widget=forms.Select(choices=ROLES_CHOICES, attrs={'class': 'border p-2 w-full'})
    )
    country = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Country'})
    )
    address = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Address'})
    )
