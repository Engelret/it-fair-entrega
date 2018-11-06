from django.shortcuts import render
from django.http import HttpResponse
from .models import PreguntasFrecuentes
from .models import Noticias
from django.shortcuts import redirect

# Create your views here.

#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login

from django.contrib.auth.decorators import login_required


def index(request):
    usuario = request.session.get('usuario',None)
    return render(request,'index.html',{'usuario':usuario})

def preguntasFrecuentes(request):
    usuario = request.session.get('usuario',None)
    return render(request,'preguntasFrecuentes.html',{'usuario':usuario,'preguntasFrecuentes':PreguntasFrecuentes.objects.all()})

@login_required(login_url='login')
def nuevaPregunta(request):
    pregunta = request.POST.get('pregunta','')
    respuesta = request.POST.get('respuesta','')
    preguntaFrecuente = PreguntasFrecuentes(pregunta=pregunta,respuesta=respuesta)
    preguntaFrecuente.save()
    return redirect('preguntasFrecuentes')

def contacto(request):
    return render(request,'contacto.html',{})

def quienesSomos(request):
    return render(request,'quienesSomos.html',{})

def noticias(request):
    usuario = request.session.get('usuario',None)
    return render(request,'noticias.html',{'usuario':usuario,'noticias':Noticias.objects.all()})

@login_required(login_url='login')
def nuevaNoticia(request):
    titulo = request.POST.get('titulo','')
    cuerpo = request.POST.get('cuerpo','')
    imagen = request.FILES.get('imagen',False)
    fuente = request.POST.get('fuente','')
    noticias = Noticias(titulo=titulo,cuerpo=cuerpo,imagen=imagen,fuente=fuente)
    noticias.save()
    return redirect('noticias')

def categorias(request):
    return render(request,'categorias.html',{})

def login(request):
    return render(request,'login.html',{})

def login_iniciar(request):
    usuario = request.POST.get('nombre_usuario','')
    contrasenia = request.POST.get('contrasenia','')
    user = authenticate(request,username=usuario, password=contrasenia)

    if user is not None:
        auth_login(request, user)
        request.session['usuario'] = user.first_name+" "+user.last_name
        return redirect("index")
    else:
        return redirect("login")


@login_required(login_url='login')
def cerrar_session(request):
    logout(request)
    return redirect('index')