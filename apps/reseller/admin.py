from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Reseller


@admin.register(Reseller)
class ResellerAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'cpf', 'created_at', 'date_joined',)
    list_display_links = list_display
    search_fields = ('email',)
    list_filter = ('created_at',)

    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password',)}),
        ('Dados pessoais', {'fields': ('cpf', )}),
        ('Permissões', {'fields': ('groups',)}),
        ('Datas importantes', {'fields': ('date_joined', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'full_name', 'cpf', 'password1', 'password2',)}),
    )
