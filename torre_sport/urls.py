from django.urls import include, path
from . import views

app_name = "crud_basket"

urlpatterns = [
    path('', views.InicioView.as_view(), name="inicio"),   
    path('inicio/', views.InicioView.as_view(), name="inicio"), 
]