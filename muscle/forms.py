from django import forms
from .models import Menu

class EditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Menu
        fields = "__all__"

class AddMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
