from django import forms
from django.forms.fields import CharField, IntegerField
from django.db.models import fields
from .models import Categoria, ProductoServicio
from applications.Proveedor.models import Proveedor

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductServicioForm(forms.ModelForm):
    class Meta:
        model = ProductoServicio
        fields = '__all__'

class Detalle_venta(forms.Form):
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        widget=forms.Select(attrs={'class':'form-control show-tick'})
    )
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs={'class':'form-control show-tick'})
    )
