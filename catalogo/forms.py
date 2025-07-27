from django import forms
from .models import ProductoModel


class ProductoForm(forms.ModelForm):
    class Meta:
        model = ProductoModel
        fields = ["nombre", "descripcion", "precio", "stock"]
