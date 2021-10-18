from django import forms
from django.forms.fields import CharField, IntegerField
from django.db.models import fields
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