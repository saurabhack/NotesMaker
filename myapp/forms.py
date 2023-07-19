# forms.py
from django import forms
from .models import AddNotes
class MyForm(forms.ModelForm):
    class Meta:
        model = AddNotes
        fields = '__all__'
        