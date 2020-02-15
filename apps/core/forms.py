from django.forms import ModelForm
import django_filters
from .models import Reseller

class ResellerFilter(django_filters.FilterSet):
    class Meta:
        model = Reseller
        fields = ('full_name',)


class ResellerForm(ModelForm):
    class Meta:
        model = Reseller
        fields = ['full_name', 'cpf']

id