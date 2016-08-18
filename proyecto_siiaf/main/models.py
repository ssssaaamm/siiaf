from django.db import models

# Create your models here.

class Empresa(models.Model):

	nombre = models.CharField(max_length=75, unique=True, null=False,)

	descripcion = models.TextField(null=True)

	class Meta:
		db_table = 'empresa'