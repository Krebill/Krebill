from django.urls import path
from .views import *
urlpatterns = [
    path('',vote,name='vote'),
        
]