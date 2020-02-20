import os
from django.conf import settings
from collections import namedtuple
from django.core.management.base import BaseCommand
from apps.reseller.models import Reseller


class Command(BaseCommand):
    def handle(self, **options):

        names = (
           'Jannat Malone',
           'Felix Brandt',
           'Isobel Valentine',
           'Samera Sheehan',
           'Ariyah Choi',
           'Karter Travers',
           'Anoushka Morgan',
           'Eden Parks',
           'Anastasia Maynard',
           'Carol Camacho',
        )

        emails = (
            'jannat@fake.com',
            'felix@fake.com',
            'isobel@fake.com',
            'samera@fake.com',
            'ariyha@fake.com',
            "karter@fake.com",
            "morgan@fake.com",
            "eden@fake.com",
            "anastasia@fake.com",
            "carol@fake.com",
        )

        cpfs = (
            '92716791058',
            '47819477008',
            '64012251066',
            '82275440020',
            '09253479060',
            '99342359000',
            '35451192030',
            '43310240088',
            '11523649011',
            '45760759000',
        )

        ResellerFake = namedtuple('Reseler', 'full_name email cpf')
        data = []
        for i in range(len(names)):
            data.append(ResellerFake(names[i], emails[i], cpfs[i]))

        id_user = 100
        success = True
        for reseller in data:
            id_user += 1
            try:
                Reseller.objects.create(
                    id=id_user,
                    full_name=reseller.full_name,
                    cpf=reseller.cpf,
                    email=reseller.email,
                    password='master123'

                )
            except Exception as e:
                success = False
                print(f'Errro no cadastro do reseller: {id_user}/{reseller.email}:')
                print('Error=>', e)

        msg = "Dados carregados com sucesso..." if success else "Falha ao carregar os dados..."
        print(msg)
