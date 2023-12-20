from django import forms
from django import *

from app1.models import *

class details(forms.ModelForm):
    class Meta:
        model=det
        fields='__all__'