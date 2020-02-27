from django.urls import reverse
import django_tables2 as tables
from django_tables2.utils import A
from .models import Reseller


class ResellerTable(tables.Table):
    # full_name = tables.LinkColumn(args=[A('pk')], attrs={'class': 'edit'}, viewname='reseller:update1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_columns['purchase_total'].verbose_name = 'Compras'
        self.base_columns['purchase_pending'].verbose_name = 'Pendente'
        self.base_columns['full_name'].verbose_name = 'Revendedor'

    class Meta:
        # template_name = "django_tables2/bootstrap4.html"
        template_name = "reseller/dt2_bs4.html"
        model = Reseller
        fields = ('full_name', 'email', 'cpf', 'purchase_total','purchase_pending')
        attrs = {"class": "table table-hover", 'thead': {'class': "thead-light"}}
        empty_text = "Não encontrado!"
