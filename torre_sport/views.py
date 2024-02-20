from django.shortcuts import render
from datetime import datetime
from . import models

# from .forms import DeporteForm, InstalacionForm, EquipoForm, JugadorForm, PartidoForm
from django.views import generic


class Inicio(generic.ListView):
    template_name = "inicio.html"
    context_object_name = "contexto"

    def get_queryset(self):
        return models.Partido.objects.all()

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["titulo"] = "Página de inicio"
        contexto["menu_opciones"] = [
            "deportes",
            "instalaciones",
            "equipos",
            "jugadores",
            "partidos",
        ]
        contexto["imagen_deporte_url"] = "URL_DE_LA_IMAGEN"
        contexto["ultimos_partidos"] = models.Partido.objects.filter(
            fecha_hora__lt=datetime.now()
        ).order_by("-fecha_hora")[:5]
        contexto["proximos_partidos"] = models.Partido.objects.filter(
            fecha_hora__gte=datetime.now()
        ).order_by("fecha_hora")[:5]
        return contexto
