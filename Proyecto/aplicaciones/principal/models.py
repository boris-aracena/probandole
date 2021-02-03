from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)#si deseo que no se repitan nombres debo agregar entre (max_length=100, unique= True) asi el valor sera unico
    apellido = models.CharField(max_length=120)
    correo = models.EmailField(max_length=200)

    def __str__(self):
        return self.nombre