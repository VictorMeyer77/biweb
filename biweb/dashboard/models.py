from django.db import models


class BMO(models.Model):
    annee = models.IntegerField()
    code_metier = models.CharField(max_length=10)
    nom_metier = models.CharField(max_length=100)
    code_famille_metier = models.CharField(max_length=3)
    nom_famille_metier = models.CharField(max_length=100)
    code_be21 = models.CharField(max_length=5)
    nom_be21 = models.CharField(max_length=100)
    code_dept = models.CharField(max_length=3)
    nom_dept = models.CharField(max_length=100)
    code_reg = models.CharField(max_length=3)
    nom_reg = models.CharField(max_length=100)
    met = models.CharField(max_length=10)
    xmet = models.CharField(max_length=10)
    smet = models.CharField(max_length=10)
