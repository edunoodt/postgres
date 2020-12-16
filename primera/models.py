from django.db import models

# Create your models here.

class general(models.Model):
    Titulo = models.CharField(max_length=40)
