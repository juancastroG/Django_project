from django.db import models

# Create your models here.
class Accesorio(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='accesorios', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.nombre
