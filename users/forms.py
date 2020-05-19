# this file will be used to create a form, which inherits from the user create form class in python
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterFrom(UserCreationForm):
    # add additional email field to the form
    email = forms.EmailField()

    # meta to describe the form
    class Meta:
        # will save to User model
        model = User
        # these will be fields in the form and the order that they will be shown
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
