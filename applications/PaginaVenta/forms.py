from django import forms
from .models import PaginaVentas
import requests
import json

class RegistrarPaginaForm(forms.ModelForm):
    """Form definition for RegistrarPagina."""

    class Meta:
        """Meta definition for RegistrarPaginaform."""
        model = PaginaVentas
        fields = '__all__'
        widgets = {
            'nombre_sitio':forms.TextInput(attrs={
                'class': 'form-control',
                'type':'text',
                'placeholder': 'Nombre del sitio'
            }),
            'descripcion':forms.TextInput(attrs={
              'class': 'form-control',
              'type': 'text',
              'placeholder': 'Descripcion del sitio'  
            }),
            'no_cuenta':forms.TextInput(attrs={
              'class': 'form-control',
              'type': 'number',
              'placeholder': 'Numero de cuenta asociada al portal financiero'  
            }),
            'status':forms.TextInput(attrs={'class': 'filled-in','type':'checkbox'})
        }
      

    def clean_no_cuenta(self):
        no_cuenta = self.cleaned_data.get('no_cuenta')
        url = 'https://httpbin.org/post'
        response = requests.post(url,data={"no_cuenta":no_cuenta})
        res_json = json.loads(response.text)
        print(res_json['form'])
        self.add_error('no_cuenta', "No existe la cuenta")    
        return no_cuenta
