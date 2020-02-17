from django import forms
import django_filters
from .models import Reseller

class ResellerFilter(django_filters.FilterSet):
    class Meta:
        model = Reseller
        fields = ('full_name',)


class ResellerForm(forms.ModelForm):
    class Meta:
        model = Reseller
        fields = ['full_name', 'cpf']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)