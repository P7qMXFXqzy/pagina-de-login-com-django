from django.db import models


class Usuarios(models.Model):
    nomeUsuario = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
