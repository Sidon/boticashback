from django.db import models
from apps.reseller.models import Reseller
from apps.cashback.models import CashbackRange, CashbackDebit, CashbackPayment
from localflavor.br.models import BRCPFField


bnull = dict(blank=True, null=True)


class Purchase(models.Model):
    STATUS = (
        ('EM_AVALIACAO', 'Em avaliação'),
        ('APROVADO', 'Aprovado'),
    )

    reseller = models.ForeignKey(Reseller, verbose_name='Revendedor', on_delete=models.PROTECT,
                                 related_name='purchases')
    code = models.CharField(verbose_name='Codigo', max_length=20)
    purchase_value = models.DecimalField(verbose_name='Valor da compra', max_digits=12, decimal_places=2)
    date_purchase = models.DateField('Data da compra')
    cashback_credit_value = models.DecimalField(verbose_name='Crédito de cashback', max_digits=12, decimal_places=2, **bnull)
    status = models.CharField(verbose_name='Status', max_length=16, choices=STATUS, default='EM_AVALIACAO')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return f'{self.reseller.full_name} - ' \
               f'{self.get_status_display()}'

    class Meta:
        ordering = ('date_purchase',)
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

    @staticmethod
    def get_cashback_to_debit_percent(value):
        ranges = CashbackRange.objects.all()
        if value and ranges:
            for rng in ranges:
                if rng.start_value <= value < rng.end_value:
                    return rng.percentage
        else:
            return 0

    @staticmethod
    def get_cashback_debit_value(value, percent=10):
        return (value * percent) / 100

    @staticmethod
    def get_cashback_credit_value(purchase_date, reseller):
        pass

    def save(self, *args, **kwargs):
        """ Populating cashback value and percentage of purchase """
        cashback_percent = Purchase.get_cashback_to_debit_percent(self.purchase_value)
        cashback_value = Purchase.get_cashback_debit_value(self.purchase_value, cashback_percent)
        created = self.pk is None
        super(Purchase, self).save(*args, **kwargs)

        if created:
            if cashback_percent:
                purchase = Purchase.objects.get(pk=self.pk)
                CashbackDebit.objects.create(
                    purchase=purchase,
                    percentage=cashback_percent,
                    cashback_value=cashback_value,
                )


class ApprovedCPF(models.Model):
    cpf = BRCPFField('CPF', unique=True)
    reseller = models.OneToOneField(Reseller, on_delete=models.CASCADE, **bnull)
    description = models.TextField('Descrição', **bnull)
    @property
    def reseller_name(self):
        return self.reseller.full_name
