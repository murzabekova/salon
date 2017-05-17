from django import forms
from clients.models import Clients


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('name', 'phone', 'email', 'comments')
    exclude = ()


class ActivationForm(forms.Form):
    your_kod = forms.CharField(label='Код потверждения', max_length=5)
