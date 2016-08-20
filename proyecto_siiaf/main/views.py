from django.shortcuts import render

# Create your views here.
def index(request):
	#La siguiente linea es solo para ejemplo
	return render(request, 'main/index.html')

def registrar_empresa(request):
	pass

def registrar_cliente(request):
	pass

def registrar_motorista(request):
	pass

def registrar_cabezal(request):
	pass

def registrar_viaje(request):
	pass

def configurar_politica_pago(request):
	pass

def configurar_politica_cobro(request):
	pass

