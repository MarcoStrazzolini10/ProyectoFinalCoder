from django.db import models

# Create your models here.
class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen', null=True, black=True )
    description = models.TextField(verbose_name='Descripcion', null=True)

def __str__(self):
    fila = "Titulo:"+ self.titulo + "-" + "Descripcion:" + self.Descripcion
    return fila

def delete(self, using=None, kepp_parents=False)
    self.imagen.delete()
    super().delete()