from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name="home"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout', logout, name="logout"),
    path('registro', registro, name="registro"),
    path('addtocar/<codigo>', addtocar, name="addtocar"),
    path('dropitem/<codigo>', dropitem, name="dropitem"),
    path('limpiar', limpiar, name="limpiar"),
    path('carrito', carrito, name="carrito"),
    path('comprar', comprar, name="comprar"),
    path('seguimiento', seguimiento, name="seguimiento"),
    path("historial", historial, name="historial"),
    path('suscribir', suscribir, name="suscribir"),
]
