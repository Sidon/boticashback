import os
from random import (uniform, choices)
from decimal import Decimal
from datetime import date
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from apps.cashback.models import CashbackRange


class Command(BaseCommand):

    def handle(self, **options):
        success = True
        CashbackRange.objects.all().delete()
        fixtures_dir = os.path.join(settings.BASE_DIR, 'apps/cashback/fixtures')
        fixture_file = os.path.join(fixtures_dir, 'cashback_range.json')

        try:
            call_command('loaddata', fixture_file, verbosity=0)
        except Exception as e:
            print('Erro ao cadastrar ranges: ')
            print(e)
            success = False

        msg = "Dados carregados com sucesso..." if success else "Falha ao carregar os dados..."
        print(msg)
