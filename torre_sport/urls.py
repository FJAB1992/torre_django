from django.urls import include, path
from . import views

app_name = "torre_sport"

urlpatterns = [
    path('', views.InicioView.as_view(), name="inicio"),   
    path('inicio/', views.InicioView.as_view(), name="inicio"),
    # Deportes
    path('list_deportes/', views.DeporteListView.as_view(), name="list_deportes"), 
]