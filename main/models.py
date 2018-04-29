# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

class Cuenta(models.Model):
    no_cuenta = models.IntegerField(primary_key=True)
    cod_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='cod_usuario')
    cantidad = models.FloatField()

    class Meta:
        managed = True
        db_table = 'cuenta'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class Tipo(models.Model):
    cod_tipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'tipo'


class Transaccion(models.Model):
    no_cuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='no_cuenta')
    fecha_hora = models.DateTimeField(primary_key=True, default=timezone.now)
    monto = models.FloatField()
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    cod_tipo = models.ForeignKey(Tipo, models.DO_NOTHING, db_column='cod_tipo')

    class Meta:
        managed = True
        db_table = 'transaccion'


class Transferencia(models.Model):
    no_cuenta_origen = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='no_cuenta_origen', related_name='cuenta_origen')
    no_cuenta_destino = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='no_cuenta_destino', related_name='cuenta_destino')
    fecha_hora = models.DateTimeField(primary_key=True, default=timezone.now)
    monto = models.FloatField()

    class Meta:
        managed = True
        db_table = 'transferencia'


class Usuario(models.Model):
    cod_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=200)

    class Meta:
        managed = True
        db_table = 'usuario'
