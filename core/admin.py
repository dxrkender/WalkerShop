from django.contrib import admin

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'slug', 'is_active',)
    list_display = ('username', 'email', 'slug', 'is_active', 'date_joined',)
