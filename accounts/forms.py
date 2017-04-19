from django import forms
from django.contrib.auth.models import User


class MasterRegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label='Password confirmation')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }),
            'password_confirmation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Подтвердите пароль',
            }),
        }
        exclude = ()

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError('Пароль должен быть длинее 6 символов')
        return password

        def clean(self):
            pass


class RegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label='Password confirmation')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'password_confirmation')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
            }),
            'password_confirmation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Подтвердите пароль',
            }),
        }
        exclude = ()

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError('Пароль должен быть длинее 6 символов')
        return password
