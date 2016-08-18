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
	
	#expresion: /main/registro_viajes
	url(r'^registro_viajes/$',views.registrar_viaje, name = 'registrar_viaje'),
	
	#expresion: /main/politicas_pago/
	url(r'^politicas_pago/$',views.configurar_politica_pago, name = 'configurar_ppago'),
	
	#expresion: /main/politicas_cobro/
	url(r'^politicas_cobro/$',views.configurar_politica_cobro, name = 'configurar_pcobro'),
]
