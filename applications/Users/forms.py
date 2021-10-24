from django import forms
from django.contrib.auth import authenticate
from .models import Usuario

class UsuarioRegistroForm(forms.ModelForm):
    """Form definition for username."""
    password2 = forms.CharField(
        max_length=100,required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar contraseña',
                'minlength':'6'
            }
        )
    )
    class Meta:
        """Meta definition for usernameform."""
        model = Usuario
        fields = ('username','password','nombre')
        widgets ={
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Usuario',
                }
            ),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre Completo',
            }),
            'password': forms.TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'type':'password',
                'minlength':'6'   
            })
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = Usuario.objects.filter(username=username)
        if user:
            self.add_error('username','El usuario ya existe')
        return username
    
    def clean_FIELD(self):
        FIELD = self.cleaned_data.get('FIELD')
    
    
         # TODO Validation
    
        return FIELD

class UsuarioUpdateForm(UsuarioRegistroForm):
    """Form definition for usernameUpdate."""

    class Meta(UsuarioRegistroForm.Meta):
        """Meta definition for usernameUpdateform."""
        fields = '__all__'
        exclude = ('username',)

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder':'Usuario'
    }))
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
        attrs={
        'class': 'form-control',
        'placeholder':'Contraseña'
    }))

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            self.add_error('username','El usuario no existe')
        return password