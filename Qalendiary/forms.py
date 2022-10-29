from django import forms
from django import forms
from .models import Objetivo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ObjetivoForm(forms.ModelForm):
    class Meta:
        model=Objetivo
        exclude=["fecha","usuario"]

class NewRegister(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','password1','password2']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None