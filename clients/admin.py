from django.contrib import admin
from clients.models import Clients

# Register your models here.

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    model = Clients
    fields = ('name', 'phone', 'email', 'comments')
