from .models import file_Upload
from django import forms

class File1Upload(forms.ModelForm):
    class Meta:
        model = file_Upload
        fields = '__all__'