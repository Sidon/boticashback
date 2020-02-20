# Generated by Django 3.0.3 on 2020-02-20 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reseller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Codigo')),
                ('purchase_value', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor da compra')),
                ('date_purchase', models.DateField(verbose_name='Data da compra')),
                ('cashback_credit_value', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Crédito de cashback')),
                ('status', models.CharField(choices=[('UNDER_VALIDATION', 'Em avaliação'), ('APPROVED', 'Aprovado')], default='UNDER_VALIDATION', max_length=16, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('reseller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='purchases', to='reseller.Reseller', verbose_name='Revendedor')),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
                'ordering': ('date_purchase',),
            },
        ),
        migrations.CreateModel(
            name='ApprovedCPF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reseler', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reseller.Reseller')),
            ],
        ),
    ]
