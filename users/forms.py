from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # If we need to add different fields other than username, we add here.
    email = forms.EmailField()

    class Meta:
        # It puts all the fields together and lets the model to interact with table (here: User)
        # The fields should should be in order
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    address = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)

    class Meta:
        model = Profile
        fields = ['address', 'contact_no', 'image']
