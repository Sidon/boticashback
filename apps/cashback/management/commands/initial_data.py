import os
from random import (uniform, choices)
from decimal import Decimal
from datetime import date
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from apps.cashback.models import CashbackRange

User = get_user_model()

class Command(BaseCommand):

    def handle(self, **options):
        success = True
        CashbackRange.objects.all().delete()
        fixtures_dir = os.path.join(settings.BASE_DIR, 'apps/cashback/fixtures')
        fixture_file = os.path.join(fixtures_dir, 'cashback_range.json')
        database = 'default'
        user_data = {'password': 'Master123', 'email': 'admin@fakemail.com'}

        try:
            User.objects.all().delete()
            User._default_manager.db_manager(database).create_superuser(**user_data)
        except Exception as e:
            print('Erro ao cadastrar superuser')
            print(e)

        try:
            call_command('loaddata', fixture_file, verbosity=0)
        except Exception as e:
            print('Erro ao cadastrar ranges: ')
            print(e)
            success = False

        try:
            call_command('revendedores_iniciais', verbosity=0)
        except Exception as e:
            print('Erro ao cadastrar revendedores: ')
            print(e)
            success = False

        try:
            call_command('compras_iniciais', verbosity=0)
        except Exception as e:
            print('Erro ao cadastrar compras: ')
            print(e)
            success = False

        msg = "Dados carregados com sucesso..." if success else "Falha ao carregar os dados..."
        print(msg)
