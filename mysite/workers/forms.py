from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddWorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['fio', 'position', 'telephone', 'email', 'adress', 'photo']
