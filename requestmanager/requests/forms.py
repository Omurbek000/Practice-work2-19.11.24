from django import forms
from .models import Requests


class Form(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ["name", "email", "message"]
