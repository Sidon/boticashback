import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from apps.authcb.models import AuthcbUser


class Command(BaseCommand):
    def handle(self, **options):
        fixtures_dir = os.path.join(settings.BASE_DIR, 'apps/reseller/fixtures')
        fixture_file = os.path.join(fixtures_dir, 'initial_reseller.json')

        emails = ['jannat@fake.com', 'felix@fake.com', 'isobel@fake.com', 'samera@fake.com', 'ariyha@fake.com' ]
        id_user = 100

        success = True
        for email in emails:
            id_user += 1
            try:
                AuthcbUser.objects.create(id=id, email=email, password='master123')
            except:
                success = False
                print(f'Errro ao cadastrar: {id_user}/{email}, possivelmente o registro ja esteja cadastrado',
                      id_user, email)

        try:
            call_command('loaddata', fixture_file, verbosity=0)
        except:
            print('Erro ao cadastrar revenderores')
            success = False

        msg = "Dados carregados com sucesso..." if success else "Falha ao carregar os dados..."
        print(msg)
