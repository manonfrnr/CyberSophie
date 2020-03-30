from django.db import models

class Question(models.Model):
    enonce = models.CharField(max_length=300)
    isLibre = models.BooleanField()


class Choix(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    valeur = models.CharField(max_length=100)

class Reponse(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    valeur = models.CharField(max_length=1000)