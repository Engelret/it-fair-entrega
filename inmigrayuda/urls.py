from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name="index"),
    path('preguntasFrecuentes/',views.preguntasFrecuentes,name="preguntasFrecuentes"),
    path('preguntasFrecuentes/nuevaPregunta',views.nuevaPregunta,name="nuevaPregunta"),
    path('quienesSomos/',views.quienesSomos,name="quienesSomos"),
    path('contacto/',views.contacto,name="contacto"),
    path('noticias/',views.noticias,name="noticias"),
    path('noticias/nuevaNoticia',views.nuevaNoticia,name="nuevaNoticia"),
    path('categorias/',views.categorias,name="categorias"),
    path('login',views.login,name="login"),
    path('cerrarsession',views.cerrar_session,name="cerrar_session"),
    path('login/iniciar',views.login_iniciar,name="iniciar")
]