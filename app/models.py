from django.db import models
from django.utils import timezone

class Question(models.Model):
    enonce = models.CharField(max_length=300)
    isLibre = models.BooleanField()
    def __str__(self):
        return self.enonce


class Choix(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    valeur = models.CharField(max_length=100)
    def __str__(self):
        return str(self.question) + " // " + str(self.valeur)

    class Meta:
        verbose_name_plural = "Choix"


class Reponse(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    valeur = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de la réponse")
