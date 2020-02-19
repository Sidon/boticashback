from django import forms
from django.contrib import admin
from .models import CashbackDebit, CashbackPayment, CashbackRange


@admin.register(CashbackDebit)
class CashbackDebitAdmin(admin.ModelAdmin):
    list_display = ('purchase', 'percentage', 'cashback_value', 'status',)
    list_display_links = list_display
    search_fields = ('purchase.name',)
    list_filter = ('status',)


@admin.register(CashbackPayment)
class CashBackPaymentAdmin(admin.ModelAdmin):
    list_display = ('reseller', 'reseller_cpf')
    list_display_links = list_display

    def reseller(self, instance):
        return instance.reseller

    def reseller_cpf(self, instance):
        return instance.reseller.cpf


@admin.register(CashbackRange)
class CashbackRangeAdmin(admin.ModelAdmin):
    list_display = ('start_value', 'end_value', 'percentage',)
    list_display_links = list_display

