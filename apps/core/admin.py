from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Reseller


# @admin.register(EscritorioUser)
# class EscritorioUserAdmin(UserAdmin):
#     add_form = EscritorioUserCreationForm
#     form = EscritorioUserChangeForm
#
#     list_display = ('email', 'get_full_name',
#                     'escritorio', 'is_active',)
#     list_display_links = list_display
#     list_filter = ('is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'nome', 'password',)}),
#         ('Dados pessoais', {'fields': ('cpf', 'rg', 'oab', 'profissao', 'rep_legal', 'procurador',)}),
#         ('Permissões', {'fields': ('escritorio', 'groups',)}),
#         ('Datas importantes', {'fields': ('date_joined', 'last_login')}),
#     )
#
#     add_fieldsets = (
#         (None, {'fields': ('email', 'nome', 'escritorio', 'password1', 'password2',)}),
#     )
#     search_fields = ('email', 'name', 'escritorio__nome', 'escritorio__schema_name')
#     ordering = ('nome',)
#     filter_horizontal = ['user_permissions']
#     autocomplete_fields = ['escritorio', 'groups']
#     list_per_page = 30


@admin.register(Reseller)
class ResellerAdmin(UserAdmin):
    list_display = ('email', 'created_at', 'full_name', 'date_joined',)
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
