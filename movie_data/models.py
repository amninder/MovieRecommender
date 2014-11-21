from django.db import models


class Genere(models.Model):
    genere = models.CharField(max_length=100)
