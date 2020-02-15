from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Reseller

@admin.register(Reseller)
class ResellerAdmin(UserAdmin):
    list_display = ('email', 'created_at', 'first_name')
    list_display_links = list_display
    search_fields = ('email',)
    list_filter = ('created_at',)