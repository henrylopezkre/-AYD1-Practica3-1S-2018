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

def registrar(request):
	context = {}
	if request.method == 'POST':
		#USUARIO
		codigo = obtener_codigo()
		nombre = request.POST.get('nombre', '')
		apellido = request.POST.get('apellido', '')
		nickname = request.POST.get('nickname', '').lower()
		correo = request.POST.get('correo', '')
		contrasenia = request.POST.get('contrasenia', '')
		rep_contrasenia = request.POST.get('rep_contrasenia', '')
		usuario_obj = Usuario.objects.all().filter(nickname=nickname).first()
		#CUENTA
		no_cuenta = obtener_no_cuenta()
		cantidad = 0.00
		if usuario_obj is None:
			if contrasenia == rep_contrasenia:
				usuario_obj = Usuario(codigo=codigo, nombre=nombre, apellido=apellido, nickname=nickname, correo=correo, contrasenia=contrasenia)
				usuario_obj.save()
				#CUENTA
				if Usuario.objects.all().filter(codigo=codigo).exists():
					cuenta_obj = Cuenta(no_cuenta=no_cuenta, codigo=usuario_obj, cantidad=cantidad)
					cuenta_obj.save()
					context = {
						'codigo' : str(codigo),
						'no_cuenta' : str(no_cuenta)
					}
				else:
					context = {
						'mensaje' : 'Algo inesperado ocurrió mientras se registraba sus datos.'
					}
			else:
				context = {
					'mensaje' : 'La contraseña no coincide, vuelva a ingresarla.'
				}
		else:
			context = {
				'mensaje' : 'El nombre de usuario no se encuentra disponible.'
			}
		return render(request, 'main/registrar.html', context)
	return render(request, 'main/registrar.html', context)

def principal(request):
	return render(request, 'main/principal.html', {})

def transferir(request):
	context = {}
	if request.method == 'POST':
		no_cuenta = request.POST.get('no_cuenta', '')
		cuenta_obj_d = Cuenta.objects.all().filter(no_cuenta=no_cuenta).first()
		cuenta_obj_o = Cuenta.objects.get(no_cuenta=request.session['no_cuenta'])
		monto = request.POST.get('monto', '')
		if cuenta_obj_d is None:
			context = {
				'error' : 'El No. de cuenta no existe.'
			}
		else:
			if float(monto) > cuenta_obj_o.cantidad:
				context = {
					'error' : 'El monto solicitado es mayor al saldo de su cuenta.'
				}
			else:
				cuenta_obj_o.cantidad = cuenta_obj_o.cantidad-float(monto)
				cuenta_obj_o.save()
				cuenta_obj_d.cantidad = cuenta_obj_d.cantidad+float(monto)
				cuenta_obj_d.save()
				transferencia_obj = Transferencia(no_cuenta_origen=cuenta_obj_o, no_cuenta_destino=cuenta_obj_d, monto=monto)
				transferencia_obj.save()
				context = {
					'mensaje' : "Transferencia realizada correctamente."
				}
		return render(request, 'main/transferir.html', context)
	return render(request, 'main/transferir.html', {})

def debito_credito(request):
	context = {}
	if request.method == 'POST':
		#DEBITO_CREDITO
		tipo = request.POST.get('tipo_descripcion', '')
		no_cuenta = request.POST.get('no_cuenta', '')
		cuenta_obj = Cuenta.objects.all().filter(no_cuenta=no_cuenta).first()
		monto = request.POST.get('monto', '')
		descripcion = request.POST.get('descripcion', '')
		tipo_obj = Tipo.objects.get(descripcion=tipo)
		if cuenta_obj is None:
			context = {
				'error' : 'El No. de cuenta no existe.'
			}
		else:
			cuenta1_obj = Cuenta.objects.get(no_cuenta=request.session['no_cuenta'])
			if tipo_obj.cod_tipo == 1:
				#if float(monto) > cuenta1_obj.cantidad:
					#context = {
					#	'error' : 'El monto solicitado es mayor al saldo de su cuenta.'
					#}
				#else:
					#cuenta1_obj.cantidad = cuenta1_obj.cantidad-float(monto)
					#cuenta1_obj.save()
					cuenta_obj.cantidad = cuenta_obj.cantidad+float(monto)
					cuenta_obj.save()
					context = {
						'mensaje' : "Operación realizada correctamente."
					}
			elif tipo_obj.cod_tipo == 2:
				if float(monto) > cuenta_obj.cantidad:
					context = {
						'error' : 'El monto solicitado es mayor al saldo de la cuenta a debitar.'
					}
				else:
					cuenta_obj.cantidad = cuenta_obj.cantidad-float(monto)
					cuenta_obj.save()
					context = {
						'mensaje' : "Operación realizada correctamente."
					}
			transaccion_obj = Transaccion(no_cuenta=cuenta_obj, monto=monto, descripcion=descripcion, cod_tipo=tipo_obj)
			transaccion_obj.save()
		return render(request, 'main/debito_credito.html', context)
	return render(request, 'main/debito_credito.html', {})

def obtener_no_cuenta():
	cuenta = Cuenta.objects.all().last()
	return cuenta.no_cuenta+1

def obtener_codigo():
	usuario = Usuario.objects.all().last()
	return usuario.codigo+1