from django.contrib import admin

from account.models import Client


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'slug', 'is_active',)
    list_display = ('username', 'email', 'slug', 'is_active', 'date_joined',)




