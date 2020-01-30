from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    inicio = models.DateField()
    fim = models.DateField()