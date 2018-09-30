from django.db import models

# Create your models here.

class producto(models.Model):
	id_producto = models.CharField(max_length=255)
	nombre = models.TextField()
	descripcion = models.TextField()
	precio = models.IntegerField(default=0)
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	votos_total = models.IntegerField(default=1)

	def __str__(self):
		return self.title

		