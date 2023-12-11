from django import forms
from .models import Profiles
from .choices import GENDER_CHOICES, ROLES_CHOICES
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Email'}),
        label='Email'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Password'}),
        label='Password'
    )

class CreateUsersForm(forms.ModelForm):
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Confirm Password'}),
        label='Confirm Password'
    )

    class Meta:
        model = Profiles
        fields = ['email', 'first_name', 'last_name', 'image', 'Tel', 'gender', 'roles', 'country', 'address']

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Email'}),
        label='Email'
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Password'}),
        label='Password'
    )

    first_name = forms.CharField(
        max_length=100,  widget=forms.TextInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'First Name'}),
        label='First Name'
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Last Name'}),
        label='Last Name'
    )
    image = forms.ImageField(
        required=False, widget=forms.FileInput(attrs={'class': 'border p-2 w-full mb-4'}),
        label='Profile Image'
    )
    Tel = forms.CharField(
        max_length=10, widget=forms.TextInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Phone', 'type': 'tel'}),
        label='Phone'
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'border p-2 w-full'}),
        label='Gender'
    )
    
    country = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Country'}),
        label='Country'
    )
    address = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={'class': 'border p-2 w-full', 'placeholder': 'Address'}),
        label='Address'
    )
