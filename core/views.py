from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *    
import requests

def historial(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    ventas = Venta.objects.filter(cliente=request.user)
    context = {"ventas":ventas}
    suscrito(request, context)
    return render(request, 'core/historial.html', context)

def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total 
    venta.save()
    for item in carro:
        detalle = DetalleVenta()
        producto = Productos.objects.get(codigo=item[0])
        detalle.producto = Productos.objects.get(codigo = item[0])
        detalle.precio = item[4]
        detalle.cantidad = item[5]
        detalle.venta = venta
        producto.stock -= item[5]
        detalle.save()
        producto.save()
        request.session["carro"] = []
    return redirect(to="carrito")

def carrito(request):
    context = {}
    carro = request.session.get("carro", [])
    suscrito(request, context)
    context["carro"] = carro
    return render(request, 'core/compras.html', context)

def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[5] >= 1:
                item[5] -= 1
                item[6] = item[4] * item[5]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carrito")

def addtocar(request, codigo):
    producto = Productos.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[5] += 1
            item[6] = item[4] * item[5]
            break
    else:
        carro.append([codigo, producto.nombre, producto.descripcion, producto.imagen, producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect(to="home")

def limpiar(request):
    request.session.flush()
    return redirect(to="carrito")

def home(request):
    produ = Productos.objects.all()
    context = {'produ':produ}
    carro = request.session.get("carro", [])
    suscrito(request, context)
    context["carro"] = carro
    return render(request, 'core/index.html', context)

def suscribir(request):
    context = {}
    suscrito(request, context)
    if not request.user.is_authenticated:
        return redirect(to="login")
    if request.method == "POST":
        if request.user.is_authenticated:
            resp = requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}")
            context["mensaje"] = resp.json()["mensaje"]
            suscrito(request, context)
        return render(request, 'core/suscripcion.html', context)
    else:
        suscrito(request, context)
        return render(request, 'core/suscripcion.html', context)

def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp = requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]


def login(request):
    return render(request, 'core/login.html')

def logout(request):
    return logout_then_login(request, login_url="home")

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'core/registro.html', {'form':registro})

def seguimiento(request):
    context = {}
    suscrito(request, context)
    return render(request, 'core/seguimiento.html', context)