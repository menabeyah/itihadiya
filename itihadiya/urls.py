"""
URL configuration for itihadiya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from agence import views as agence_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', agence_views.accueil, name='accueil'),  # PAGE D’ACCUEIL
    path('agences/', include('agence.urls')),  
]
