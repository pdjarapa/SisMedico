from django.db import models

class Contacto(models.Model):

	nombres=models.CharField(max_length=30,blank=True)
	apellidos=models.CharField(max_length=30)
	cedula=models.CharField(max_length=30)
	email=models.EmailField()

def __str__(self):
	return self.email
