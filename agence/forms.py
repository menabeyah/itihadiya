from django import forms
from .models import Agence
from .models import Billet


class AgenceForm(forms.ModelForm):
    class Meta:
        model = Agence
        fields = ['nom']
        labels = {'nom': "Nom de l'agence"}


class BilletForm(forms.ModelForm):
    class Meta:
        model = Billet
        fields = ['nom_client', 'date_depart', 'heure_depart']
