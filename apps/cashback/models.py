from django.db import models


class CashbackRange(models.Model):
    start_value = models.DecimalField(verbose_name='Valor', max_digits=12, decimal_places=2)
    end_value = models.DecimalField(verbose_name='Valor', max_digits=12, decimal_places=2)
    percentage = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Porcentagem do Cashback')

    class Meta:
        verbose_name = 'Intervalo de valores'
        verbose_name_plural = 'Intervalos de valores'
        ordering = ['-start_value']


class CashbackDebit(models.Model):
    STATUS = (
        ('PENDING', 'Pendente'),
        ('PAID', 'Pago'),
    )
    # Evitando circular import
    purchase = models.OneToOneField('purchase.Purchase', on_delete=models.PROTECT, related_name='debit')
    percentage = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Percentagem do cashback')
    cashback_value = models.DecimalField(verbose_name='Valor', max_digits=12, decimal_places=2)
    status = models.CharField('Status', max_length=8, choices=STATUS, default='PENDING')

    class Meta:
        verbose_name = 'Cashback Débito'
        verbose_name_plural = 'Cashback Débitos'

    @property
    def reseller(self):
        return self.purchase.reseller

    @property
    def date_purchase(self):
        return self.purchase.date_purchase

    def __str__(self):
        return f'{self.purchase.code} - ' \
               f'{self.get_status_display()}'


class CashbackPayment(models.Model):
    cashbak_debit = models.OneToOneField(CashbackDebit, on_delete=models.PROTECT, related_name='cashback_payments')
    purchase = models.OneToOneField('purchase.Purchase', on_delete=models.PROTECT, related_name='purchases_refunds')
    date_payment = models.DateField('Data do pagamento')

    class Meta:
        verbose_name = 'Cashback Pagamento'
        verbose_name_plural = 'Cashback Pagamentos'

