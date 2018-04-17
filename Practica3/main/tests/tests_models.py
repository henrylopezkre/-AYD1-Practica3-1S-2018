from django.test import TestCase, RequestFactory
from django.utils import timezone
from main.models import Usuario, Cuenta, Tipo, Transferencia, Transaccion

class ModelsTestCase(TestCase):

	def create_usuario(self):
		return Usuario.objects.create(codigo=1234, nombre='Pedro', apellido='Perez', 
			nickname='pperez', correo='pperez@gmail.com', contrasenia='hola123')

	def test_usuario_creation(self):
		u = self.create_usuario()
		self.assertTrue(isinstance(u, Usuario))

	def create_tipo(self):
		return Tipo.objects.create(descripcion='Prueba')

	def test_tipo_creation(self):
		u = self.create_tipo()
		self.assertTrue(isinstance(u, Tipo))

	def create_cuenta(self):
		return Cuenta.objects.create(no_cuenta=1234567899, codigo=self.create_usuario(), cantidad=1000.00)

	def test_cuenta_creation(self):
		u = self.create_cuenta()
		self.assertTrue(isinstance(u, Cuenta))

	def create_transferencia(self):
		return Transferencia.objects.create(no_cuenta_origen=self.create_cuenta(), no_cuenta_destino=self.create_cuenta(), monto=1000.00)

	def test_transferencia_creation(self):
		u = self.create_transferencia()
		self.assertTrue(isinstance(u, Transferencia))

	def create_transaccion(self):
		return Transaccion.objects.create(no_cuenta=self.create_cuenta(), monto=1000.00, descripcion='Débito', cod_tipo=self.create_tipo())

	def test_transaccion_creation(self):
		u = self.create_transaccion()
		self.assertTrue(isinstance(u, Transaccion))