from django.contrib import admin
from .models import *


class TelefonoClienteInline(admin.TabularInline):
    model = TelefonoCliente
    extra = 0
    autocomplete_fields = ['tipo'] #BUSQUEDA SOBRE EL CAMPO


class ClienteAdmin(admin.ModelAdmin):
    inlines = [TelefonoClienteInline] #Detalles
    search_fields = ['nombre', 'apellido', 'nit', 'favorito']
    list_filter = ['genero', 'nit', 'favorito', ]
    date_hierarchy = 'fecha_nacimiento'
    list_display = ['id', 'nombre', 'apellido', 'genero', 'edad', 'nit', 'favorito']


    fieldsets = [
        ('Datos Personales', {
            'fields': (
                ('nombre', 'apellido'),
                ('fecha_nacimiento', 'genero'), 
                ('nit','favorito'),
                )
        }),
    ]

# Register your models here.
admin.site.register(Cliente, ClienteAdmin)