from enum import unique
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, unique=True)
    celular = models.CharField(max_length=11)

'''class Receita(models.Model):
    usuario_criou = user
    nome_receita = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    tempo_de_preparo = models.SmallIntegerField()
    rendimento_porcoes = models.SmallIntegerField()
    categoria = models.CharField(max_length=80)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)'''