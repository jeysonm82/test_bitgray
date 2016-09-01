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
        return "%s. %s - $%s" % (self.pk, self.producto, self.precio)

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
    precio = models.PositiveIntegerField()
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s - %s, $%s. Sede: %s" % (self.producto.producto, self.cliente, self.precio, self.sede)

    class Meta:
        managed = False
        db_table = 'compras'
        verbose_name_plural = 'compras'


class Log(models.Model):
    fecha = models.DateTimeField()
    descripcion = models.TextField()

    def __unicode__(self):
        return "%s - %s" % (self.fecha, self.descripcion)

    class Meta:
        managed = False
        db_table = 'log'
