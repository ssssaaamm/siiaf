from django.db import models

# Create your models here.

class Cliente(models.Model):

	nombre = models.CharField(max_length=75, unique=True)

	descripcion = models.TextField(null=True)

	class Meta:
		db_table = 'cliente'
		

class Empresa(models.Model):

	nombre = models.CharField(max_length=75, unique=True)

	descripcion = models.TextField(null=True)

	clientes = models.ManyToManyField( Cliente, through='Afiliacion', through_fields=('empresa','cliente') )

	class Meta:
		#Forzar nombre de la tabla en la base de datos
		db_table = 'empresa'


class Afiliacion(models.Model):

	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

	class Meta:
		db_table = 'afiliacion'


class Motorista(models.Model):

	codigo = models.CharField(max_length=10, primary_key=True)

	nombre = models.CharField(max_length=50)

	licencia = models.CharField(max_length=20, unique=True)

	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

	class Meta:
		db_table = 'motorista'


class Cabezal(models.Model):

	placa = models.CharField(max_length=20)

	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

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

	class Meta:
		db_table = 'politica_pago'


class PeriodoFacturacion(models.Model):

	inicio = models.DateTimeField()

	fin = models.DateTimeField()
	
	actual = models.BooleanField()
	
	politica_cobro = models.ForeignKey(PoliticaCobro)


class PeriodoPlanilla(models.Model):

	inicio = models.DateTimeField()

	fin = models.DateTimeField()

	actual = models.DateTimeField()

	politica_pago = models.ForeignKey(PoliticaPago)