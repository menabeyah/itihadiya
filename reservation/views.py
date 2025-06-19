from django.http import JsonResponse
from django.shortcuts import render , redirect
from .models import Trajet
from .forms import ReservationForm
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from .models import Trajet, Reservation
from .models import Ville
from django.shortcuts import get_object_or_404
from .models import Reservation
from django.contrib import messages



def liste_trajets(request):
    trajets = Trajet.objects.all()
    return render(request, 'reservation/liste_trajets.html', {'trajets': trajets})

def reserver(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            
            if request.user.is_authenticated:
                reservation.utilisateur = request.user  # Associer l'utilisateur connecté
            
            trajet = reservation.trajet

            # Vérifier la disponibilité
            if reservation.nombre_places <= trajet.places_disponibles:
                trajet.places_disponibles -= reservation.nombre_places
                trajet.save()
                reservation.save()

                # Envoyer email de confirmation
                sujet = 'Confirmation de votre réservation - Itihadiya'
                message = f"""
Bonjour {reservation.nom_client},

Votre réservation a bien été enregistrée !

Trajet : {trajet.depart} → {trajet.arrivee}
Date : {trajet.date_depart.strftime('%d/%m/%Y %H:%M')}
Nombre de places : {reservation.nombre_places}
Prix total : {trajet.prix * reservation.nombre_places} MRU

Merci d’avoir utilisé Itihadiya !
                """
                send_mail(
                    sujet,
                    message,
                    'tonemail@gmail.com',  # Remplace par ton adresse e-mail
                    [reservation.email],
                    fail_silently=False
                )

                return redirect('confirmation')
            else:
                form.add_error('nombre_places', f"Il ne reste que {trajet.places_disponibles} places disponibles.")
    else:
        form = ReservationForm()

    return render(request, 'reservation/reserver.html', {'form': form})

def confirmation(request):
    # Si tu récupères la dernière réservation :
    reservation = Reservation.objects.filter(utilisateur=request.user).last()
    return render(request, 'reservation/confirmation.html', {'reservation': reservation})
    
def get_places_disponibles(request):
    trajet_id = request.GET.get('trajet_id')
    try:
        trajet = Trajet.objects.get(id=trajet_id)
        return JsonResponse({'places_disponibles': trajet.places_disponibles})
    except Trajet.DoesNotExist:
        return JsonResponse({'error': 'Trajet non trouvé'}, status=404)
    
def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            utilisateur = form.save()
            login(request, utilisateur)
            return redirect('liste_trajets')
    else:
        form = UserCreationForm()
    return render(request, 'reservation/inscription.html', {'form': form})

@login_required
def mes_reservations(request):
    reservations = Reservation.objects.filter(utilisateur=request.user)
    return render(request, 'reservation/mes_reservations.html', {'reservations': reservations})


@staff_member_required
def tableau_de_bord(request):
    total_trajets = Trajet.objects.count()
    total_reservations = Reservation.objects.count()
    reservations_par_trajet = Reservation.objects.values('trajet__depart__nom', 'trajet__arrivee__nom').annotate(total=Count('id'))

    return render(request, 'reservation/tableau_de_bord.html', {
        'total_trajets': total_trajets,
        'total_reservations': total_reservations,
        'reservations_par_trajet': reservations_par_trajet
    })

def liste_villes(request):
    villes = Ville.objects.all()
    return render(request, 'reservation/liste_villes.html', {'villes': villes})

def payer(request, reservation_id):
    # plus tard : intégrer Stripe, CinetPay, PayPal, etc.
    messages.info(request, "Le paiement en ligne sera disponible bientôt.")
    reservation = get_object_or_404(Reservation, id=reservation_id, utilisateur=request.user)
    reservation.paiement_effectué = True
    reservation.save()
    return redirect('confirmation')

@login_required
def mon_compte(request):
    reservations = Reservation.objects.filter(utilisateur=request.user)
    return render(request, 'reservation/mon_compte.html', {'reservations': reservations})

def get_places_disponibles(request):
    trajet_id = request.GET.get('trajet_id')
    try:
        trajet = Trajet.objects.get(id=trajet_id)
        return JsonResponse({'places_disponibles': trajet.places_disponibles})
    except Trajet.DoesNotExist:
        return JsonResponse({'error': 'Trajet introuvable'}, status=404)