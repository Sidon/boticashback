from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRCPFField

User = get_user_model()


class ResellerManager(models.Manager):
    def create_reseller(self, email, full_name, cpf, password):
        user = self.model(
            email=email,
            full_name=full_name,
            cpf=cpf
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Reseller(User):
    cpf = BRCPFField('CPF', unique=True)
    full_name = models.CharField('Nome Completo', max_length=70)
    objects = ResellerManager()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Revendedor'
        verbose_name_plural = 'Revendedores'


