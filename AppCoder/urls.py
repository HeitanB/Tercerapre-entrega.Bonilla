from django.urls import path

from AppCoder import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('Equipos', views.equipos, name="Equipos"),
    path('dt', views.dt, name="DT"),
    path('jugadores', views.jugadores, name="Jugadores"),
    path('entregables', views.entregables, name="Entregables"),
    #path('equipoFormulario', views.equipoFormulario, name="EquipoFormulario"),
    #path('dtFormulario', views.dtFormulario, name="DTFormulario"),
    #path('busquedaPosición',  views.busquedaPosición, name="BusquedaPosición"),
    path('buscar/', views.buscar),
   
]

