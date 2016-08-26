from django.conf.urls import url
from . import views

app_name='main' #para crear namespace local
urlpatterns = [
	
	#expresion: /main/
	url(r'^$',views.index, name = 'index'), #cada aplicacion puede tener su propio index
	
	#expresion: /main/empresas/...
	url(r'^empresas/$',views.empresas,name = 'empresas'),
	url(r'^empresas/crear/$',views.crear_empresa, name = 'crear_empresa'),
	url(r'^empresas/actualizar/(?P<empresa_id>[0-9]+)/$',views.actualizar_empresa, name = 'actualizar_empresa'),
	url(r'^empresas/eliminar/(?P<empresa_id>[0-9]+)/$',views.eliminar_empresa, name = 'eliminar_empresa'),
	
	#expresion: /main/clientes/...
	url(r'^clientes/$',views.clientes, name = 'clientes'),
	#url(r'^clientes/crear/$',views.crear_cliente, name = 'crear_cliente'),
	#url(r'^clientes/actualizar/(?P<cliente_id>[0-9]+)/$',views.actualizar_cliente, name = 'actualizar_cliente'),
	#url(r'^clientes/eliminar/(?P<cliente_id>[0-9]+)/$',views.eliminar_cliente, name = 'eliminar_cliente'),

	#expresion: /main/motoristas/...
	url(r'^motoristas/$',views.motoristas, name = 'motoristas'),
	#url(r'^motoristas/crear/$',views.crear_motorista, name = 'crear_motorista'),
	#url(r'^motoristas/actualizar/(?P<motorista_id>[0-9]+)/$',views.actualizar_motorista, name = 'actualizar_motorista'),
	#url(r'^motoristas/eliminar/(?P<motorista_id>[0-9]+)/$',views.eliminar_motorista, name = 'eliminar_motorista'),

	#expresion: /main/cabezales/...
	url(r'^cabezales/$',views.motoristas, name = 'cabezales'),
	#url(r'^cabezales/crear/$',views.crear_motorista, name = 'crear_cabezal'),
	#url(r'^cabezales/actualizar/(?P<cabezal_id>[0-9]+)/$',views.actualizar_motorista, name = 'actualizar_cabezal'),
	#url(r'^cabezales/eliminar/(?P<cabezal_id>[0-9]+)/$',views.eliminar_motorista, name = 'eliminar_cabezal'),
	
	#expresion: /main/viajes
	url(r'^viajes/$',views.viajes, name = 'viajes'),
	
	#expresion: /main/politicas_pago/
	url(r'^politicas_pago/$',views.configurar_politica_pago, name = 'configurar_politica_pago'),
	
	#expresion: /main/politicas_cobro/
	url(r'^politicas_cobro/$',views.configurar_politica_cobro, name = 'configurar_politica_cobro'),
]
