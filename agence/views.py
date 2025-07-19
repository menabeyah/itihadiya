from django.shortcuts import render, get_object_or_404, redirect
from .models import Agence, Billet
from .forms import BilletForm, AgenceForm

def liste_agences(request):
    agences = Agence.objects.all()
    return render(request, 'agence/liste_agences.html', {'agences': agences})

def ajouter_agence(request):
    if request.method == 'POST':
        form = AgenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_agences')
    else:
        form = AgenceForm()
    return render(request, 'agence/ajouter_agence.html', {'form': form})

def reserver_billet(request, agence_id):
    agence = get_object_or_404(Agence, id=agence_id)

    if request.method == 'POST':
        form = BilletForm(request.POST)
        if form.is_valid():
            billet = form.save(commit=False)
            billet.agence = agence
            billet.save()
            return redirect('accueil')
    else:
        form = BilletForm()
    
    return render(request, 'agence/reserver_billet.html', {'form': form, 'agence': agence})

def accueil(request):
    agences = Agence.objects.all()
    return render(request, 'accueil.html', {'agences': agences})
