# coding: utf-8
from django import forms
# from django.contrib.auth.models import User
from profiles.models import MasterProfile


class ProfileForm(forms.ModelForm):
    class Meta():
        model = MasterProfile
        fields = ('user', 'first_name', 'last_name', 'fillial', 'master_type', 'image', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
            }),
        }
        exclude = ()
