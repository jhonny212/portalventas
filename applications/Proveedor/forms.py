from django import forms
from django.forms import widgets
from django.forms.fields import CharField, DateField, DateTimeField, IntegerField
from django.db.models import fields
from django.forms.models import ModelChoiceField
from .models import *

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        exclude = ()
    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        self.fields['proveedor']= CharField(label="Proveedor", required=True) 
        self.fields['telefono']= IntegerField(label="Telefono", required=True,min_value=0) 
        self.fields['direccion']= CharField(label="Direccion", required =False)

class AsignacionProveedorForm(forms.ModelForm):
    class Meta:
        model = AsignacionProveedor
        fields = ('id_proveedor', 'id_producto')
    def __init__(self, *args, **kwargs):
        aux = kwargs.pop('aux')
        if aux == 0:
            otros_productos = kwargs.pop('otros_productos')
            id_proveedor = kwargs.pop('id_proveedor')
        else:
            id_producto = kwargs.pop('id_producto')
            otros_proveedores = kwargs.pop('otros_proveedores')

        super(AsignacionProveedorForm, self).__init__(*args, **kwargs)

        if aux == 1:
            self.fields['id_proveedor'] = ModelChoiceField(queryset=otros_proveedores, label="Proveedor", required=True, empty_label='Seleccione un Proveedor')
            self.fields['id_producto'].initial = id_producto
        else:
            self.fields['id_proveedor'].initial = id_proveedor
            self.fields['id_producto'] = ModelChoiceField(queryset=otros_productos, label="Producto",required=True, empty_label='Seleccione un Producto')

class LoteForm(forms.ModelForm):
    class Meta:
        model = LoteProducto
        fields = '__all__'
        widgets = {
            'proveedor':forms.Select(attrs={
              'class': 'form-control show-tick',
            }),
            'cantidad':forms.NumberInput(attrs={
              'class': 'form-control',
              'type': 'number',
              'placeholder': 'Cantidad',
              'min':'0',
              'onchange':'setTwoNumberDecimal',
              'step':'1',
              'required':'False'
            })
        }


    def __init__(self, *args, **kwargs):
        aux = kwargs.pop('aux')
        if aux == 0:
            otros_productos = kwargs.pop('otros_productos')
            id_proveedor = kwargs.pop('proveedor')
        else:
            id_producto = kwargs.pop('producto')
            otros_proveedores = kwargs.pop('otros_proveedores')

        super(LoteForm, self).__init__(*args, **kwargs)
        self.fields['fecha_ingreso']= DateField(required =False) 

        if aux == 1:
            self.fields['proveedor'] = ModelChoiceField(queryset=otros_proveedores, label="Proveedor", required=True, empty_label='Seleccione un Proveedor')
            self.fields['producto'].initial = id_producto
        else:
            self.fields['proveedor'].initial = id_proveedor
            self.fields['producto'] = ModelChoiceField(queryset=otros_productos, label="Producto",required=True, empty_label='Seleccione un Producto')