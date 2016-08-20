from django.conf.urls import url
from . import views

app_name='main' #para crear namespace local
urlpatterns = [
	
	#expresion: /main/
	url(r'^$',views.index, name = 'index'), #cada aplicacion puede tener su propio index
	
	#expresion: /main/registro_empresas/
	url(r'^registro_empresas/$',views.registrar_empresa, name = 'registrar_empresa'),
	
	#expresion: /main/registro_clientes
	url(r'^registro_clientes/$',views.registrar_cliente, name = 'registrar_cliente'),

	#expresion: /main/registro_motoristas/
	url(r'^registro_motoristas$',views.registrar_motorista, name = 'registrar_motorista'),

	#expresion: /main/registro_cabezales/
	url(r'^registro_cabezales$',views.registrar_motorista, name = 'registrar_cabezal'),
	
	#expresion: /main/registro_viajes
	url(r'^registro_viajes/$',views.registrar_viaje, name = 'registrar_viaje'),
	
	#expresion: /main/politicas_pago/
	url(r'^politicas_pago/$',views.configurar_politica_pago, name = 'configurar_politica_pago'),
	
	#expresion: /main/politicas_cobro/
	url(r'^politicas_cobro/$',views.configurar_politica_cobro, name = 'configurar_politica_cobro'),
]
