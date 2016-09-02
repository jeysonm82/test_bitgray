from __future__ import unicode_literals

from django.db import models

# ORM models for database.


class Clientes(models.Model):
    documento = models.IntegerField()
    nombres = models.CharField(max_length=80)
    detalles = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.documento, self.nombres)

    class Meta:
        managed = False
        db_table = 'clientes'
        verbose_name_plural = 'clientes'


class Productos(models.Model):
    producto = models.CharField(max_length=40)
    precio = models.PositiveIntegerField()
    descripcion = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "%s. %s - $%s (Desc: %s)" % (self.pk, self.producto, self.precio, self.descripcion)

    class Meta:
        managed = False
        db_table = 'productos'
        verbose_name_plural = 'productos'


class Sedes(models.Model):
    sede = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)

    def __unicode__(self):
        return "%s. %s - %s" % (self.pk, self.sede, self.direccion)

    class Meta:
        managed = False
        db_table = 'sedes'
        verbose_name_plural = 'sedes'


class Compras(models.Model):
    cliente = models.ForeignKey(
        Clientes, db_column='id_cliente', null=True, blank=True)
    producto = models.ForeignKey(
        Productos, db_column='id_producto', null=True, blank=True)
    sede = models.ForeignKey(Sedes, db_column='id_sede', null=True, blank=True)
    precio = models.PositiveIntegerField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s - %s, $%s. Sede: %s" % (self.producto.producto, self.cliente, self.precio, self.sede)

    def get_precio(self):
        # Get precio from self.producto if precio is null here
        return self.precio if self.precio is not  None else self.producto.precio

    class Meta:
        managed = False
        db_table = 'compras'
        verbose_name_plural = 'compras'


class Log(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    descripcion = models.TextField()

    def __unicode__(self):
        return "%s - %s" % (self.fecha, self.descripcion)

    class Meta:
        managed = False
        db_table = 'log'

# Signals for logging of UPDATE/DELETE queries
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

@receiver(pre_save, sender=Compras)
@receiver(pre_save, sender=Clientes)
@receiver(pre_save, sender=Productos)
@receiver(pre_save, sender=Sedes)
def signal_update(sender, **kwargs):
    instance = kwargs['instance']
    try:
        pre_instance = instance.__class__.objects.get(pk=instance.pk)
    except:
        pre_instance = None
    action = 'UPDATE' if pre_instance is not None else 'CREATE'
    log_msg = "ACTION: %s \n Instance id: %s \n previous value: %s \n new value: %s"%(action, instance.pk, pre_instance, instance)
    log = Log()
    log.descripcion = log_msg
    log.save()
    
@receiver(post_delete, sender=Compras)
@receiver(post_delete, sender=Clientes)
@receiver(post_delete, sender=Productos)
@receiver(post_delete, sender=Sedes)
def signal_delete(sender, **kwargs):
    instance = kwargs['instance']
    log_msg = "ACTION: DELETE \n Instance id: %s \n previous value: %s"%(instance.pk, instance)
    log = Log()
    log.descripcion = log_msg
    log.save()
