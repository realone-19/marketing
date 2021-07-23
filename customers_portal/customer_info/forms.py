from django import forms
from django.contrib.auth.models import User
from . import models


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','first_name','last_name','password')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = models.UserProfileInfo
        fields = ('phone_number',)
