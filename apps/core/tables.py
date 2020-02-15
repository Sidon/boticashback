from django.urls import reverse
import django_tables2 as tables
from django_tables2.utils import A
from .models import Reseller


class ResellerTable(tables.Table):
    # full_name = tables.LinkColumn(args=[A('pk')], attrs={'class': 'edit'}, viewname='core:update1')

    class Meta:
        # template_name = "django_tables2/bootstrap4.html"
        template_name = "core/dt2_bs4.html"
        model = Reseller
        fields = ('full_name', 'user_name', 'profile_url',)
        attrs = {"class": "table table-hover", 'thead': {'class': "thead-light"}}
        empty_text = "Não encontrado!"
