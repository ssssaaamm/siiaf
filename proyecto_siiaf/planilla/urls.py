from django.conf.urls import url
from . import views

app_name='planilla' #para crear namespace local
urlpatterns = [
	#expresion: /planilla/
	url(r'^$',views.index, name = 'index'), #cada aplicacion puede tener su propio index
]