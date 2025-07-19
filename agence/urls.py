from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_agences, name='liste_agences'),
    path('ajouter/', views.ajouter_agence, name='ajouter_agence'),
    path('reserver/<int:agence_id>/', views.reserver_billet, name='reserver_billet'),

]
