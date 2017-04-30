# coding: utf-8
from django import forms
# from django.contrib.auth.models import User
from profiles.models import MasterProfile


class ProfileForm(forms.ModelForm):
    class Meta():
        model = MasterProfile
        fields = ('fillial', 'master_type', 'image', 'email')
        widgets = {
            'fillial': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Филлиал',
            }),
            'master_type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Тип работы',
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Аватар',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
            }),
        }
        exclude = ()
