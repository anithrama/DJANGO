from django import forms
from .models import *

class Emform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
