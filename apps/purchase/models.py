from django.db import models
from djmoney.models.fields import MoneyField
from apps.reseller.models import Reseller
from apps.cashback.models import CashbackRange, CashbackDebit, CashbackPayment



class Purchase(models.Model):
    STATUS = (
        ('UNDER_VALIDATION', 'Em avaliação'),
        ('APPROVED', 'Aprovado'),
    )

    reseller = models.ForeignKey(Reseller, verbose_name='Revendedor', on_delete=models.PROTECT, related_name='purchases')
    code = models.CharField(verbose_name='Codigo', max_length=20)
    value = MoneyField(verbose_name='Valor', max_digits=12, decimal_places=2, default_currency='BRL')
    date_purchase = models.DateField('Data da compra')
    status = models.CharField(verbose_name='Status', max_length=16, choices=STATUS, default='UNDER_VALIDATION')
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
    def get_cashback_percent(value):
        ranges = CashbackRange.objects.all()
        if value and ranges:
            for rng in ranges:
                if rng.start_value <= value < rng.end_value:
                    return rng.percentage
        else:
            return 0

    @staticmethod
    def get_cashback_value(value, percent):
        return (value * percent) / 100



    def save(self, *args, **kwargs):
        """ Populating cashback value and percentage of purchase """
        cashback_percent = Purchase.get_cashback_percent(self.value)
        cashback_value = Purchase.get_cashback_value(self.value, cashback_percent)
        created = self.pk is None
        super(Purchase, self).save(*args, **kwargs)

        print('created ==>', created)
        print('cashback_percent-->', cashback_percent)

        if created and cashback_percent:
            purchase = Purchase.objects.get(pk=self.pk)
            CashbackDebit.objects.create(
                purchase=purchase,
                percentage=cashback_percent,
                cashback_value=cashback_value,
            )


class ApprovedCPF(models.Model):
    reseler = models.OneToOneField(Reseller, on_delete=models.CASCADE)
    @property
    def reseller_name(self):
        return self.reseler.full_name

