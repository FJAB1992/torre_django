from django.urls import include, path
from . import views

app_name = "torre_sport"

urlpatterns = [
    path('', views.InicioView.as_view(), name="inicio"),   
    path('inicio/', views.InicioView.as_view(), name="inicio"),
    # Deportes
    path('list_deportes/', views.DeporteListView.as_view(), name="list_deportes"),
    # Equipos
    path('list_equipos/', views.EquipoListView.as_view(), name="list_equipos"), 
    # Instalaciones
    path('list_instalaciones/', views.InstalacionListView.as_view(), name="list_instalaciones"),
    # Jugadores
    path('list_jugadores/', views.JugadorListView.as_view(), name="list_jugadores"), 
    # Partidos
    path('list_partidos/', views.PartidoListView.as_view(), name="list_partidos"),    
]