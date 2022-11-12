from django.db import models
from persona.models import Persona, TipoTelefono

# Create your models here.
class Cliente(Persona):
    nit = models.CharField('NIT', max_length=10, unique=True, null=True, blank=True, default='C/F')
    favorito = models.BooleanField(default=True)

    class Meta():
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        unique_together = ['nombre', 'apellido']
    
    def __str__(self):
        return "%s - %s" % (self.nit, self.nombre)

class TelefonoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField('telefono')
    predeterminado = models.BooleanField(default=True)
    tipo = models.ForeignKey(
        TipoTelefono, verbose_name='Tipo Telefono', related_name='TelCliente', on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s %s" % (self.cliente, self.numero)

    class Meta():
        db_table = 'telefono_cliente'
        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'
