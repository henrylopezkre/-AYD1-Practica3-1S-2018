from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Usuario, Cuenta, Transaccion, Transferencia, Tipo
# Create your views here.

def index(request):
    return render(request, 'main/index.html', {})

def iniciar_sesion(request):
	context = {}
	if request.method == 'POST':
		#CREDENCIALES
		codigo = request.POST.get('codigo', '')
		nickname = request.POST.get('nickname', '')
		contrasenia = request.POST.get('contrasenia', '')
		usuario = Usuario.objects.all().filter(codigo=codigo, nickname=nickname, contrasenia=contrasenia).first()
		if usuario is None:
			context = {
				'mensaje' : 'Credenciales no existen.'
			}
		else:
			cuenta = Cuenta.objects.get(codigo=codigo)
			request.session['codigo'] = usuario.codigo
			request.session['nickname'] = usuario.nickname
			request.session['no_cuenta'] = cuenta.no_cuenta
			return redirect('main:principal')
	return render(request, 'main/iniciar_sesion.html', context)

def cerrar_sesion(request):
	del request.session['codigo']
	del request.session['nickname']
	del request.session['no_cuenta']
	return redirect('main:index')

def principal(request):
	return render(request, 'main/principal.html', {})