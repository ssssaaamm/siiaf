from django.conf.urls import url
from . import views

app_name='facturacion' #para crear namespace local
urlpatterns = [
	#expresion: /facturacion/
	url(r'^$',views.index, name = 'index'), #cada aplicacion puede tener su propio index
]