from django.test import TestCase
from django.utils import timezone
from .models import Usuario, Cuenta, Transaccion, Transferencia, Tipo

class UsuarioTestCase(TestCase):
	def create_usuario(self):
		#tipo1 = Tipo.objects.create(descripcion='Préstamo')
		return Usuario.objects.create(nombre='Pedro', apellido='Perez', nickname='pperez', correo='pperez@gmail.com', contrasenia='hola123')
		#cuenta1 = Cuenta.objects.create(codigo=usuario1, cantidad=100.00)
		#cuenta2 = Cuenta.objects.create(codigo=usuario2, cantidad=200.00)
		#Transferencia.objects.create(no_cuenta_origen=cuenta1, no_cuenta_destino=usuario2, monto=50.00)
		#Transaccion.objects.create(monto=75.00, descripcion='Nuevo préstamo', cod_tipo=tipo1)

	def test_usuario_creation(self):
		self.assertEqual(2, len(Usuario.objects.all()))
		#u = self.create_usuario()
		#self.assertTrue(isinstance(w, Usuario))
#		usuario1 = Usuario.objects.get(nombre='Pedro')
#		self.assertEqual(usuario1.apellido, 'Perez')