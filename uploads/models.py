from django.db import models

class Archivo(models.Model):
    archivo = models.FileField(upload_to="archivos/")
    subido_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.archivo.name