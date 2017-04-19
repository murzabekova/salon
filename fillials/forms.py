from django import forms
# from django.contrib.auth.models import User
from fillials.models import Fillials


class FillialsForm(forms.ModelForm):
    class Meta():
        model = Fillials
        fields = ('title', 'description', 'image')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование',
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
                'placeholder': 'Выберите файл',
            }),
        }
        exclude = ()
