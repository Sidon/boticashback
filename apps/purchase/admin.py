from django.contrib import admin
from .models import Purchase, ApprovedCPF


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('reseller_fullname', 'date_purchase', 'code', 'purchase_value', 'cashback_percentage',
                    'cashback_value', 'status',)

    list_display_links = list_display
    search_fields = ('code',)

    def reseller_fullname(self, instance):
        return instance.reseller.full_name

    def cashback_percentage(self, instance):
        return instance.debit.percentage

    def cashback_value(self, instance):
        return instance.debit.cashback_value


@admin.register(ApprovedCPF)
class ApprovedCPF(admin.ModelAdmin):
    list_display = ('reseller', 'reseller_cpf')
    list_display_links = list_display

    def reseller(self, instance):
        return instance.reseller

    def reseller_cpf(self, instance):
        return instance.reseller.cpf
