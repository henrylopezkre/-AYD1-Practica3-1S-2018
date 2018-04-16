# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class Cuenta(models.Model):
    no_cuenta = models.IntegerField(primary_key=True)
    codigo = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='codigo')
    cantidad = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cuenta'


class Tipo(models.Model):
    cod_tipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo'


class Transaccion(models.Model):
    no_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='no_cuenta', primary_key=True)
    fecha_hora = models.DateTimeField(default=datetime.now, blank=True, primary_key=True)
    monto = models.FloatField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    cod_tipo = models.ForeignKey(Tipo, models.DO_NOTHING, db_column='cod_tipo')

    class Meta:
        managed = False
        db_table = 'transaccion'
        unique_together = (('no_cuenta', 'fecha_hora'),)


class Transferencia(models.Model):
    no_cuenta_origen = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='no_cuenta_origen', related_name='cuenta_origen')
    no_cuenta_destino = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='no_cuenta_destino', related_name='cuenta_destino')
    fecha_hora = models.DateTimeField(default=datetime.now, blank=True, primary_key=True)
    monto = models.FloatField()

    class Meta:
        managed = False
        db_table = 'transferencia'
        unique_together = (('no_cuenta_origen', 'no_cuenta_destino', 'fecha_hora'),)


class Usuario(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'usuario'
