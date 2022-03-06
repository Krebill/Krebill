from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('projet/<str:pk>/', projetpage, name='projet'),
    
    path('ajou-projet/', ajoutprojet, name='ajout'),
    path('Modifier-projet/<str:pk>/', modifier, name='modifier'),
    
    path('Inbox/', inbox, name="inbox"),
    path('Message/<str:pk>/', messagepage, name="message"),
    
    path('ajoutskill/', ajoutskill, name="skill"),
    path('ajoutendo/', ajoutendo, name="endo"),
    
    path('donation/', pourboire, name='boire'),
    path('charts/', chartpage, name='chart')
    
    
]