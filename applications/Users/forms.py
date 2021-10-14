from django import forms
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

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        if self.cleaned_data.get('password')!=password2:
            self.add_error('password2','Las contraseñas no coinciden')

class UsuarioUpdateForm(UsuarioRegistroForm):
    """Form definition for usernameUpdate."""

    class Meta(UsuarioRegistroForm.Meta):
        """Meta definition for usernameUpdateform."""
        exclude = ('username',)
