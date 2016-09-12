from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Empresa, Cliente
from .forms import EmpresaForm, ClienteForm, MotoristaForm

# Create your views here.
def index(request):
	#La siguiente linea es solo para ejemplo
	return render(request, 'main/index.html', {'form':EmpresaForm(initial={'clientes': [Cliente.objects.get(nombre='COCA'),Cliente.objects.get(nombre='TROPIGAS')]})})

def empresas(request):
	pass

def crear_empresa(request):
	pass		


def actualizar_empresa(request,empresa_id):
	pass		


def eliminar_empresa(request,empresa_id):
	pass



def clientes(request):
	pass

def motoristas(request):
	pass

def cabezales(request):
	pass

def viajes(request):
	pass

def configurar_politica_pago(request):
	pass

def configurar_politica_cobro(request):
	pass

