from django import forms
from django.utils.translation import ugettext as _
from . import models
from django.contrib.auth.models import User


class UploadLabForm(forms.ModelForm):
    class Meta:
        model = models.Lab
        fields = ('name', 'course')


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ('name', )


class RegisterUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'first_name', 'last_name')


class LoginUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')