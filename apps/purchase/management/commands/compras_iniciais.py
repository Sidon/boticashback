import os
from random import (uniform, choices)
from decimal import Decimal
from datetime import date
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from apps.purchase.models import Purchase


class Command(BaseCommand):

    def handle(self, **options):
        ids = 101, 102, 103, 104, 103, 101, 105, 106, 107, 108, 109, 110, 107, 107
        success = True

        for n in range(20):
            chcs = choices(ids, k=6)
            for reseller in chcs:
                purchase_value = uniform(1, 4687)
                try:
                    Purchase.objects.create(
                        reseller_id=reseller,
                        purchase_value=Decimal(purchase_value),
                        date_purchase=date.today()

                    )
                except Exception as e:
                    success = False;
                    print('Value==>', Decimal(purchase_value))
                    print('Error-->', e)

        msg = "Dados carregados com sucesso..." if success else "Falha ao carregar os dados..."
        print(msg)
