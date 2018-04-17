from django.test import TestCase, RequestFactory
from django.utils import timezone
from main.views import obtener_no_cuenta, obtener_codigo, iniciar_sesion, registrar, transferir, debito_credito, saldo, principal, index

class ViewsTestCase(TestCase):
	def setUp(self):
        self.factory = RequestFactory()
        self.type = Tipo.objects.create(descripcion='Prueba')
        self.user = Usuario.objects.create(codigo=1234, nombre='Pedro', apellido='Perez', 
			nickname='pperez', correo='pperez@gmail.com', contrasenia='hola123')
        self.account =  Cuenta.objects.create(no_cuenta=1234567899, codigo=self.user, cantidad=1000.00)
        self.transference = Transferencia.objects.create(no_cuenta_origen=self.account,
        	no_cuenta_destino=self.account, monto=1000.00)
        self.transaccion = Transaccion.objects.create(no_cuenta=self.account, monto=1000.00, 
        	descripcion='Débito', cod_tipo=self.type)

    def test_iniciar_sesion(self):
        request = self.factory.post('main/iniciar_sesion')
        request.user = self.user
        response = iniciar_sesion(request)
        response = iniciar_sesion.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_registrar(self):
        request = self.factory.post('main/registrar')
        request.user = self.user
        response = registrar(request)
        response = registrar.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_transferir(self):
        request = self.factory.post('main/transferir')
        request.user = self.user
        response = transferir(request)
        response = transferir.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_debito_credito(self):
        request = self.factory.post('main/debito_credito')
        request.user = self.user
        response = debito_credito(request)
        response = debito_credito.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_saldo(self):
        request = self.factory.get('main/saldo')
        response = saldo(request)
        response = saldo.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_principal(self):
        request = self.factory.get('main/principal')
        response = principal(request)
        response = principal.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        request = self.factory.get('main/index')
        response = index(request)
        response = index.as_view()(request)
        self.assertEqual(response.status_code, 200)

	def test_obtener_no_cuenta(self):
		response = obtener_no_cuenta()
		self.assertEqual(response, 1234567900)

	def test_obtener_codigo(self):
		response = obtener_no_cuenta()
		self.assertEqual(response, 123457)