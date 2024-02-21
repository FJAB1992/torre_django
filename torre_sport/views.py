from django.shortcuts import render
from datetime import datetime
from . import models
from . import views

# from .forms import DeporteForm, InstalacionForm, EquipoForm, JugadorForm, PartidoForm
from django.views import generic

class InicioView(generic.ListView):
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


# class InicioView(generic.ListView):
#     template_name = "inicio.html"
#     model = models.Deporte

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context["instalaciones"] = models.Instalacion.objects.all()
#     #     context["equipos"] = models.Equipo.objects.all()
#     #     context["jugadores"] = models.Jugador.objects.all()
#     #     context["partidos"] = models.Partido.objects.all()
#     #     context["deportes"] = models.Deporte.objects.all()
#     #     return context
