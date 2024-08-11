from django.db import models

class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    Nome = models.TextField(max_length=255)
    senha = models.TextField()
