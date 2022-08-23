from django import forms 
from .models import *
  
class AvaliacaoForm(forms.ModelForm): 
  
    class Meta: 
        model = Avaliacao
        fields = ['nome', 'texto', 'img']