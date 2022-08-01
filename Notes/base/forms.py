from django import forms
from .models import DataN
from dataclasses import field


class upForm(forms.ModelForm):
    class Meta:
        model =DataN
        fields ="__all__"