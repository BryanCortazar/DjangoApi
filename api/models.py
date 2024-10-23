from django.db import models

# Create your models here.
class Genero(models.Model):
    genero = models.CharField(max_length=50, primary_key=True)  # Asegúrate de establecer un max_length apropiado
    tipo_genero = models.CharField(max_length=255)
    
    class Meta:
        db_table = "generos"

class Usuario(models.Model):
    usuario_id = models.CharField(max_length=50, primary_key=True)  # Asegúrate de establecer un max_length apropiado
    nombre_completo = models.CharField(max_length=255)
    fk_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "usuarios"
  
        