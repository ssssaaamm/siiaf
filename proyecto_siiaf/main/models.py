from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):

	nombre = models.CharField(max_length=75, unique=True)
	
	descripcion = models.TextField(null=True)

	def __str__(self):
		return self.nombre

	class Meta:
		db_table = 'cliente'
		

class Empresa(models.Model):

	nombre = models.CharField(max_length=75, unique=True)
	
	descripcion = models.TextField(null=True)
	
	clientes = models.ManyToManyField( Cliente, through='Afiliacion', through_fields=('empresa','cliente') )

	def __str__(self):
		return self.nombre
	
	class Meta:
		#Forzar nombre de la tabla en la base de datos
		db_table = 'empresa'


class Afiliacion(models.Model):

	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

	def __str__(self):
		return self.empresa__nombre + '-' + self.cliente__nombre

	class Meta:
		db_table = 'afiliacion'


class Motorista(models.Model):

	codigo = models.CharField(max_length=10, primary_key=True)

	nombre = models.CharField(max_length=50)

	licencia = models.CharField(max_length=20, unique=True)

	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

	class Meta:
		db_table = 'motorista'


class Cabezal(models.Model):

	placa = models.CharField(max_length=20, primary_key=True)

	descripcion = models.TextField(null=True)

	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

	def __str__(self):
		return self.placa

	class Meta:
		db_table = 'cabezal'


class PoliticaCobro(models.Model):

	duracion_periodo = models.IntegerField()

	tarifa_cobro_km_sen = models.FloatField()

	tarifa_cobro_km_car = models.FloatField()

	tarifa_cobro_km_vac = models.FloatField()

	tarifa_sobrepeso = models.FloatField()

	tarifa_cruce_frontera = models.FloatField()

	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

	def __str__(self):
		return self.id

	class Meta:
		db_table = 'politica_cobro'


class PoliticaPago(models.Model):

	duracion_periodo = models.IntegerField()

	salario_minimo = models.FloatField()

	porcentaje_isss = models.FloatField()
	porcentaje_afp = models.FloatField()

	tarifa_pago_km_loc = models.FloatField()
	tarifa_pago_km_int = models.FloatField()

	porcentaje_sobrepeso = models.FloatField()

	tarifa_viatico_vv = models.FloatField()
	tarifa_viatico_vc = models.FloatField()
	tarifa_viatico_cc = models.FloatField()

	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

	def __str__(self):
		return self.id

	class Meta:
		db_table = 'politica_pago'


class PeriodoFacturacion(models.Model):

	inicio = models.DateTimeField()

	fin = models.DateTimeField()
	
	actual = models.BooleanField()
	
	politica_cobro = models.ForeignKey(PoliticaCobro, on_delete=models.CASCADE)

	def __str__(self):
		return self.inicio + '--' + self.fin

	class Meta:
		db_table = 'periodo_facturacion'


class PeriodoPlanilla(models.Model):

	inicio = models.DateTimeField()

	fin = models.DateTimeField()

	actual = models.DateTimeField()

	politica_pago = models.ForeignKey(PoliticaPago, on_delete=models.CASCADE)

	def __str__(self):
		return self.inicio + '--' + self.fin

	class Meta:
		db_table = 'periodo_planilla'


class DetalleCobro(models.Model):

	total_viajes_locales = models.IntegerField(default=0)
	total_km_sen_locales = models.FloatField(default=0.0)
	total_km_car_locales = models.FloatField(default=0.0)
	total_km_vac_locales = models.FloatField(default=0.0)
	total_km_locales = models.FloatField(default=0.0)
	total_mont_sen_locales = models.FloatField(default=0.0)
	total_mont_car_locales = models.FloatField(default=0.0)
	total_mont_vac_locales = models.FloatField(default=0.0)
	total_mont_locales = models.FloatField(default=0.0)


	total_viajes_internacionales = models.IntegerField(default=0)
	total_km_sen_internacionales = models.FloatField(default=0.0)
	total_km_car_internacionales = models.FloatField(default=0.0)
	total_km_vac_internacionales = models.FloatField(default=0.0)
	total_km_internacionales = models.FloatField(default=0.0)
	total_mont_sen_internacionales = models.FloatField(default=0.0)
	total_mont_car_internacionales = models.FloatField(default=0.0)
	total_mont_vac_internacionales = models.FloatField(default=0.0)
	total_mont_internacionales = models.FloatField(default=0.0)


	total_cantidad_agregados = models.IntegerField(default=0)
	total_mont_agregados = models.FloatField(default=0.0)


	periodo_facturacion = models.ForeignKey(PeriodoFacturacion, on_delete=models.CASCADE)

	afiliacion = models.ForeignKey(Afiliacion, on_delete=models.CASCADE)

	def __str__(self):
		return self.afiliacion__cliente__nombre + '-' + self.afiliacion__empresa__nombre + '---' + self.periodo_facturacion__inicio + '-' + self.periodo_facturacion__fin

	class Meta:
		db_table = 'detalle_cobro'


class DetallePago(models.Model):

	total_viajes_locales = models.IntegerField(default=0)
	total_km_locales = models.FloatField(default=0.0)
	total_monto_locales = models.FloatField(default=0.0)

	total_viajes_internacionales = models.IntegerField(default=0)
	total_km_internacionales =  models.FloatField(default=0.0)
	total_monto_internacionales = models.FloatField(default=0.0)

	total_cantidad_agregados = models.IntegerField(default=0)
	total_monto_agregados = models.FloatField(default=0.0)
	
	total_cantidad_viaticos_vv = models.IntegerField(default=0)
	total_cantidad_viaticos_vc = models.IntegerField(default=0)
	total_cantidad_viaticos_cc = models.IntegerField(default=0)
	total_cantidad_viaticos = models.IntegerField(default=0)

	total_monto_viaticos_vv = models.FloatField(default=0.0)
	total_monto_viaticos_vc = models.FloatField(default=0.0)
	total_monto_viaticos_cc = models.FloatField(default=0.0)
	total_monto_viaticos = models.FloatField(default=0.0)

	salario_ganado = models.FloatField(default=0.0)

	delta_salario_minimo = models.FloatField(default=0.0)

	bono = models.FloatField(default=0.0)

	total_pago_periodo = models.FloatField(default=0.0)#no podra ser menor al salario minimo

	isss = models.FloatField()

	afp = models.FloatField()

	motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)

	periodo_planilla = models.ForeignKey(PeriodoPlanilla, on_delete=models.CASCADE)

	def __str__(self):
		return self.motorista__nombre + '---' + self.periodo_planilla__inicio

	class Meta:
		db_table = 'detalle_pago'


class Viaje(models.Model):

	tipo = models.CharField(max_length=1) # I-> Internacional, L->local

	fecha_registro = models.DateTimeField(default=timezone.now)

	total_km = models.FloatField()

	viatico = models.BooleanField(default=False)

	tipo_viatico = models.CharField(max_length=2)# VV,VC,CC

	periodo_facturacion = models.ForeignKey(PeriodoFacturacion, on_delete=models.CASCADE)

	periodo_planilla = models.ForeignKey(PeriodoPlanilla, on_delete=models.CASCADE)

	motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)

	cabezal = models.ForeignKey(Cabezal, on_delete=models.CASCADE)

	def __str__(self):
		return self.id


	class Meta:
		db_table = 'viaje'


class Boleta(models.Model):

	codigo = models.CharField(max_length=10, primary_key=True)

	destino = models.CharField(max_length=50)

	kilometros_asignados = models.FloatField()

	tipo_carga = models.CharField(max_length=1)# V->vacio, C->cargado, S->sencillo

	sobrepeso = models.BooleanField(default=False)

	cruce_frontera = models.BooleanField(default=False)

	sentido = models.CharField(max_length=1)# I->Ida, R->Regreso, N->Ninguno

	viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)

	def __str__(self):
		return self.codigo

	class Meta:
		db_table = 'boleta'


