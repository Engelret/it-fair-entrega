from django.db import models

# Create your models here.



class PreguntasFrecuentes(models.Model):
    pregunta = models.CharField(max_length=50)
    respuesta = models.CharField(max_length=100)
    def __str__(self):
        return "Pregunta: "+self.pregunta+" Respuesta: "+self.respuesta

class Noticias(models.Model):
    titulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos/')
    fuente = models.CharField(max_length=100)
    def __str__(self):
        return "titulo: "+self.titulo+" cuerpo: "+self.cuerpo+" imagen: "+self.imagen+" fuente: "+self.fuente