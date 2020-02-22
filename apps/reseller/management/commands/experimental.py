import os
from django.conf import settings
from collections import namedtuple
from django.contrib.auth import get_user_model
from django.contrib.auth.management import get_default_username
from django.core.management.base import BaseCommand
from apps.reseller.models import Reseller


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel = get_user_model()
        self.username_field = self.UserModel._meta.get_field(self.UserModel.USERNAME_FIELD)

    def handle(self, **options):
        user_data = {}
        pass
