from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nom_client', 'email', 'trajet', 'nombre_places']
        widgets = {
            'nom_client': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'trajet': forms.Select(attrs={'class': 'form-control'}),
            'nombre_places': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

    def clean(self):
        cleaned_data = super().clean()
        trajet = cleaned_data.get('trajet')
        nombre_places = cleaned_data.get('nombre_places')

        if trajet and nombre_places:
            if nombre_places > trajet.places_disponibles:
                raise ValidationError(
                    f"Il ne reste que {trajet.places_disponibles} places disponibles pour ce trajet."
                )
