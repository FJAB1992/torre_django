from django import forms
from . import models

class DeporteForm(forms.ModelForm):

    class Meta:
        # Asociamos al formulario del modelo Test (en models, lo llamamos así)
        model = models.Deporte
        fields = [
            "nombre",
        ]  # "__all__" ; en caso de que quiera traerme todos los campos

        widgets = { "nombre": forms.TextInput(attrs={"class": "form-control"}), }
