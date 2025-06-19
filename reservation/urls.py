from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_trajets, name='liste_trajets'),
    path('reserver/', views.reserver, name='reserver'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('ajax/places/', views.get_places_disponibles, name='get_places_disponibles'),
    path('inscription/', views.inscription, name='inscription'),
    path('mes-reservations/', views.mes_reservations, name='mes_reservations'),
    path('admin/tableau/', views.tableau_de_bord, name='tableau_de_bord'),
    path('villes/', views.liste_villes, name='liste_villes'),
    path('payer/<int:reservation_id>/', views.payer, name='payer'),
    path('mon-compte/', views.mon_compte, name='mon_compte'),
    path('ajax/places/', views.get_places_disponibles, name='get_places_disponibles'),






]
