from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils import timezone
from main.models import Usuario, Cuenta
from main.views import registrar, obtener_cod

class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = Usuario.objects.create(cod_usuario=123456, nombre='Pedro', apellido='Perez', 
			nickname='pperez', correo='pperez@gmail.com', contrasenia='hola123')
        self.account =  Cuenta.objects.create(no_cuenta=1234567899, cod_usuario=self.user, cantidad=1000.00)

    def test_registrar(self):
        request = self.factory.post('main/registrar')
        request.user = self.user
        response = registrar(request)
        self.assertEqual(response.status_code, 200)

    def test_registrar_codigo(self):
        c = obtener_cod(self.user)
        self.assertEqual(c, 123457)

