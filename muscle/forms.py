from django import forms
from .models import Menu, Record, Part

class AddMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"
