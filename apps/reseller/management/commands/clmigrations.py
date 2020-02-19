from django.core.management.base import BaseCommand, CommandError
from subprocess import PIPE, Popen
from boticashback.settings.base import BASE_DIR as DIR

PYC = 'find '+DIR+' -path "*/migrations/*.pyc"  -delete'
PY = 'find '+DIR+' -path "*/migrations/*.py" -not -name "__init__.py" -delete'


class Command(BaseCommand):
    help = 'Clean migrations directories'

    def handle(self, *args, **options):
        p = Popen(PYC, shell=True, stdout=PIPE)
        p = Popen(PY, shell=True, stdout=PIPE)
        self.stdout.write('Ok')
