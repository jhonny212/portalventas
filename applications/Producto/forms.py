from django import forms
from django.forms.fields import CharField, IntegerField
from django.db.models import fields
from .models import Categoria, ProductoServicio

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductServicioForm(forms.ModelForm):
    class Meta:
        model = ProductoServicio
        fields = '__all__'