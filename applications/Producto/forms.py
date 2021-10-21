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
        widgets = {
            'nombre':forms.TextInput(attrs={
                'class': 'form-control',
                'type':'text',
                'placeholder': 'Nombre del sitio'
            }),
            'precio':forms.NumberInput(attrs={
              'class': 'form-control',
              'type': 'number',
              'placeholder': 'Precio en Quetzales',
              'min':'0',
              'onchange':'setTwoNumberDecimal',
              'step':'0.1',
              'value':'0.00'
            }),
            'id_categoria':forms.Select(attrs={
              'class': 'form-control show-tick',
            }),
            'id_pagina_ventas':forms.Select(attrs={
              'class': 'form-control show-tick',  
            }),
            'cantidad':forms.NumberInput(attrs={
              'class': 'form-control',
              'type': 'number',
              'placeholder': 'Cantidad',
              'min':'0',
              'onchange':'setTwoNumberDecimal',
              'step':'1',
              'value':'0'
            })
        }