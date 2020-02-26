from collections import namedtuple
from django.core.management.base import BaseCommand
from apps.cashback.models import CashbackDebit
from apps.reseller.models import Reseller
from apps.purchase.models import Purchase


class Command(BaseCommand):
    def handle(self, **options):

        CashbackDebit.objects.all().delete()
        Purchase.objects.all().delete()
        Reseller.objects.all().delete()

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
           'Frank Vincent Zappa'
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
            'frank@zappa.net',
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
            '78432782815',
        )

        ResellerFake = namedtuple('Reseler', 'full_name email cpf')
        data = []
        for i in range(len(names)):
            data.append(ResellerFake(names[i], emails[i], cpfs[i]))

        id_user = 100
        success = True
        for d in data:
            id_user += 1
            try:
                reseller = Reseller()
                reseller.id = id_user
                reseller.full_name = d.full_name
                reseller.email = d.email
                reseller.cpf = d.cpf
                reseller.set_password('master123')
                reseller.save()
            except Exception as e:
                success = False
                print(f'Errro no cadastro do reseller: {id_user}/{reseller.email}:')
                print('Error=>', e)

        msg = "Dados carregados com sucesso..." if success else "Falha ao carregar os dados..."
        print(msg)
