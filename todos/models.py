from django.db import models

class usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    Nome = models.TextField(max_length=255)
    senha = models.TextField()
