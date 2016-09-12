from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Empresa, Cliente, Motorista, Cabezal, Viaje, Boleta

class EmpresaForm(forms.ModelForm):


	#declaracion explicita de campo (para mayor control sobre el)
	clientes = forms.ModelMultipleChoiceField(
		queryset=Cliente.objects.all(),
		label = 'Clientes',
		widget=forms.SelectMultiple(attrs={'class':('selectpicker form-control'), 'data-live-search':'true', 'title':'Clientes'}),
		error_messages={'invalid_choice':'Cliente no valido'},
		required=False,
	)

	class Meta:
		model = Empresa
		fields = ['nombre','descripcion','clientes']
		widgets = {
			'nombre':forms.TextInput( attrs={'class':('form-control'),'placeholder':'Nombre Empresa'} ),
			'descripcion':forms.TextInput( attrs={'class':('form-control'),'placeholder':'Descripcion Empresa','required':False}),
		}
		error_messages = {
			'nombre': {
				'max_length': _('Nombre de empresa demaciao largo'),
				'unique': _('Nombre de empresa duplicado'),
				'required': _('Nombre de empresa es requerido'),
			},
		}
		labels = {
			'nombre':_('Nombre'),
			'descripcion':_('Descripcion'),
		}
		# help_texts = {
		# 	'nombre': _('Escriba el nombre de la empresa'),
		# 	'descripcion': _('Escriba una descripcion para la empresa'),
		# }

	def clean(self):
		cleaned_data = super(EmpresaForm,self).clean()
		nombre_empresa = cleaned_data.get('nombre')
		id_clientes = cleaned_data.get('clientes')
		afiliaciones1 = Afiliacion.objects.filter(empresa__nombre=nombre_empresa)
		afiliaciones2 = []
		for id_cliente in id_clientes:
			if Afiliacion.objects.get(empresa__nombre=nombre_empresa,cliente__id=id_c).exists():
				a = Afiliacion.objects.get(empresa__nombre=nombre_empresa,cliente__id=id_c)
				afiliaciones2.apend(a)
		for afiliacion in afiliaciones1:
			if afiliacion not in afiliaciones2:
				if afiliacion.viajes_set.count() >=1:
					raise forms.ValidationError("No puede se puede desasociar con el cliente "+afiliacion.cliente__nombre)





class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = ['nombre','descripcion']
		widgets = {
			'nombre':forms.TextInput( attrs={'class':('form-control'),'placeholder':'Nombre de empresa cliente'} ),
			'descripcion':forms.TextInput( attrs={'class':('form-control'),'placeholder':'Escriba una brebe descripcion para este cliente','required':False} ),
		}
		error_messages = {
			'nombre': {
				'max_length': _('Nombre de cliente demaciao largo'),
				'unique': _('Nombre de cliente duplicado'),
				'required': _('Nombre del cliente es requerido')
			},
		}
		labels = {
			'nombre':_('Nombre'),
			'descripcion':_('Descripcion'),
		}


class MotoristaForm(forms.ModelForm):

	#declaracion explicita de campo (para mayor control sobre el)
	empresa = forms.ModelChoiceField(
		queryset=Empresa.objects.all(),
		label = 'Empresa',
		widget=forms.Select(attrs={'class':('selectpicker'), 'data-live-search':'true'}),
		error_messages={'required':'Debe escoger una empresa', 'invalid_choice':'Empresa no valida'}
	)

	class Meta:
		model = Motorista
		fields = ['codigo','nombre','licencia','empresa']
		widgets = {
			'codigo':forms.TextInput( attrs={'class':('form-control'),'placeholder':'Codigo de motorista'} ),
			'nombre':forms.TextInput( attrs={'class':('form-control'),'placeholder':'Nombre de motorista'} ),
			'licencia':forms.TextInput( attrs={'class':('form-control'),'placeholder':'Licencia del motorista'} ),
			#'empresa':forms.Select( attrs={'class':('selectpicker'), 'data-live-search':'true'}),
		}
		error_messages = {
			'codigo': {
				'max_length': _('Codigo de motorista demaciado largo'),
				'unique': _('Codigo de motorista duplicado'),
				'required': _('Codigo del motorista es requerido'),
			},
			'nombre': {
				'max_length': _('Nombre demaciado largo'),
				'required': _('Nombre de motorista es requerido'),
			},
			'licencia':{
				'max_length': _('Licencia invalida'),
				'unique': _('Licencia duplicada'),
				'required': _('Licencia es requerida'),
			},
			# 'empresa':{
			# 	'required': _('Debe seleccionar una empresa'),
			# 	'invalid_choice': _('No se ha seleccionado una empresa valida'),
			# },
		}
		labels = {
			'codigo': _('Codigo'),
			'nombre': _('Nombre'),
			'licencia': _('Licencia'),
			#'empresa': _('Empresa'),
		}
