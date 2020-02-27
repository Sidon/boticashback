from django.contrib.auth import get_user_model
from django.db import models
from localflavor.br.models import BRCPFField

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

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


    def _get_purchase_total(self):
        from apps.purchase import models as md
        sum = \
        md.Purchase.objects.filter(reseller_id=self.id).aggregate(models.Sum('purchase_value'))[
            'purchase_value__sum']
        return locale.currency(sum, grouping=True, symbol=None)

    def _get_purchase_pending(self):
        from apps.purchase import models as md
        sum = \
        md.Purchase.objects.filter(reseller_id=self.id, status='EM_AVALIACAO').aggregate(models.Sum('purchase_value'))[
            'purchase_value__sum']
        return locale.currency(sum, grouping=True, symbol=None)

    purchase_pending = property(_get_purchase_pending)
    purchase_total = property(_get_purchase_total)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Revendedor'
        verbose_name_plural = 'Revendedores'
