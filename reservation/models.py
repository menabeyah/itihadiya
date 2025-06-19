from django.db import models
from django.contrib.auth.models import User

class Ville(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Trajet(models.Model):
    depart = models.ForeignKey(Ville, related_name='depart', on_delete=models.CASCADE)
    arrivee = models.ForeignKey(Ville, related_name='arrivee', on_delete=models.CASCADE)
    date_depart = models.DateTimeField()
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    places_disponibles = models.PositiveIntegerField(default=50)  # ex: 50 places max

    def __str__(self):
        return f"{self.depart} → {self.arrivee} ({self.date_depart})"


class Reservation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nom_client = models.CharField(max_length=100)
    email = models.EmailField()
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    nombre_places = models.PositiveIntegerField()
    paiement_effectué = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom_client} - {self.trajet}"