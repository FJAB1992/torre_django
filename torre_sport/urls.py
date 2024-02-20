from django.urls import path
from . import views

# app_name = "torre_urls"

urlpatterns = [
    # Vista inicial
    path("", views.Inicio.as_view(), name="inicio"),
    
    # Vistas CRUD
    # path("listado/", views.ListadoView.as_view(), name="listado"),
    # path("detalle/<int:pk>/", views.DetalleView.as_view(), name="detalle"),
    # path("nuevo/", views.NuevoView.as_view(), name="nuevo"),
    # path("actualizar/<int:pk>/", views.ActualizarView.as_view(), name="actualizar"),
    # path("borrar/<int:pk>/", views.BorrarView.as_view(), name="borrar"),
]