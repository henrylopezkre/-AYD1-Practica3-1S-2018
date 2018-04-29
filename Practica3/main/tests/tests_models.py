from django.test import TestCase, RequestFactory
from django.utils import timezone
from main.models import Usuario, Cuenta, Tipo, Transferencia, Transaccion

class ModelsTestCase(TestCase):
	def setUp(self):
		u0 = Usuario.objects.create(cod_usuario=123456, nombre='Pedro', apellido='Perez', 
			nickname='pperez', correo='pperez@gmail.com', contrasenia='hola123')
		u1 = Usuario.objects.create(cod_usuario=123457, nombre='Maria', apellido='Castro', 
			nickname='mcastro', correo='mcastro@gmail.com', contrasenia='hola123')
		self.c0 = Cuenta.objects.create(no_cuenta=1234567899, cod_usuario=u0, cantidad=1000.00)
		self.c1 = Cuenta.objects.create(no_cuenta=1234567900, cod_usuario=u1, cantidad=2000.00)
		self.t1 = Tipo.objects.create(descripcion='Débito')
		self.t2 = Tipo.objects.create(descripcion='Crédito')


	def test_usuario_creation(self):
	 	u = Usuario.objects.get(cod_usuario=123456)
	 	self.assertTrue(isinstance(u, Usuario))

	def test_usuario_registered(self):
	 	u = Usuario.objects.get(cod_usuario=123456)
	 	self.assertEqual(u.correo, 'pperez@gmail.com')

	def create_transferencia(self):
		return Transferencia.objects.create(no_cuenta_origen=self.c0, 
			no_cuenta_destino=self.c1, fecha_hora=timezone.now(), monto=100.00)

	def test_transferencia_creation(self):
	  	tf = self.create_transferencia()
	  	self.assertTrue(isinstance(tf, Transferencia))

	def test_cuenta_destino_exists(self):
		tf = self.create_transferencia()
		self.assertTrue(tf.no_cuenta_destino.no_cuenta==1234567900)

	def test_monto_exists(self):
		tf = self.create_transferencia()
		self.assertTrue(tf.no_cuenta_origen.cantidad > tf.monto)

	def test_saldo_exists(self):
		tf = self.create_transferencia()
		self.assertTrue(tf.no_cuenta_origen.cantidad==1000.00)

	def create_debito(self):
		return Transaccion.objects.create(no_cuenta=self.c1, fecha_hora=timezone.now(), 
			monto=500.00, descripcion='Débito', cod_tipo=self.t1)

	def create_credito(self):
		return Transaccion.objects.create(no_cuenta=self.c1, fecha_hora=timezone.now(), 
			monto=80.00, descripcion='Crédito', cod_tipo=self.t2)

	def test_debito_destino_exists(self):
		deb = self.create_debito()
		self.assertTrue(deb.no_cuenta.no_cuenta==1234567900)

	def test_credito_destino_exists(self):
		cred = self.create_credito()
		self.assertTrue(cred.no_cuenta.no_cuenta==1234567900)

	def test_debito_saldo_exists(self):
		deb = self.create_debito()
		self.assertTrue(deb.no_cuenta.cantidad > deb.monto)

	def test_credito_saldo_exists(self):
		cred = self.create_credito()
		self.assertTrue(cred.no_cuenta.cantidad > cred.monto)