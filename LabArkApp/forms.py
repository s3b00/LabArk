from django import forms
from django.utils.translation import ugettext as _
from . import models


class UploadLabForm(forms.ModelForm):
    class Meta:
        model = models.Lab
        fields = ('name', 'variant', 'category', 'year', 'course', 'file')
