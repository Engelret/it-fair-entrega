from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('preguntasFrecuentes/',views.preguntasFrecuentes,name="preguntasFrecuentes"),
    path('quienesSomos/',views.quienesSomos,name="quienesSomos"),
    path('contacto/',views.contacto,name="contacto"),
    path('noticias/',views.noticias,name="noticias"),
]