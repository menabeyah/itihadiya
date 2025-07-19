from django.db import models

class Agence(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Billet(models.Model):
    agence = models.ForeignKey('agence.Agence', on_delete=models.CASCADE)
    nom_client = models.CharField(max_length=100)
    date_depart = models.DateField()
    heure_depart = models.TimeField()

    def __str__(self):
        return f"{self.nom_client} - {self.agence.nom}"