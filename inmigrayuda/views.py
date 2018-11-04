from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html',{})

def preguntasFrecuentes(request):
    return render(request,'preguntasFrecuentes.html',{})

def contacto(request):
    return render(request,'contacto.html',{})

def quienesSomos(request):
    return render(request,'quienesSomos.html',{})

def noticias(request):
    return render(request,'noticias.html',{})

def categorias(request):
    return render(request,'categorias.html',{})