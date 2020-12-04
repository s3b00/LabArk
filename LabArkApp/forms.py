from django import forms
from django.utils.translation import ugettext as _

class UserRegisterForm(forms.Form):
    username = forms.CharField(label=_(u'Username'), max_length=30)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)