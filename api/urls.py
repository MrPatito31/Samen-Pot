from django.urls import path
from .views import*

urlpatterns = [
    path('suscrito/<email>', suscrito),
    path('suscribir/<email>', suscribir),
]
