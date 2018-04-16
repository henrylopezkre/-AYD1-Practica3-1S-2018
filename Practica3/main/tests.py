from django.test import TestCase
from .models import Usuario, Cuenta, Transaccion, Transferencia, Tipo

class CuentaTestCase(TestCase):
	def setUp(self):
		tipo1 = Tipo.objects.create(descripcion='Préstamo')
		usuario1 = Usuario.objects.create(nombre='Pedro', apellido='Perez', nickname='pperez', correo='pperez@gmail.com', contrasenia='hola123')
		usuario2 = Usuario.objects.create(nombre='Maria', apellido='Perez', nickname='mperez', correo='mperez@gmail.com', contrasenia='hola123')
		cuenta1 = Cuenta.objects.create(codigo=usuario1, cantidad=100.00)
		cuenta2 = Cuenta.objects.create(codigo=usuario2, cantidad=200.00)
		Transferencia.objects.create(no_cuenta_origen=cuenta1, no_cuenta_destino=usuario2, monto=50.00)
		Transaccion.objects.create(monto=75.00, descripcion='Nuevo préstamo', cod_tipo=tipo1)

	def test_cantidad(self):
		cuenta1 = Cuenta.objects.get(cantidad=100.00)
		self.assertEqual(cuenta1.cantidad, 100.00)
