from django import forms
from .models import Pessoa


class PessoaForm(forms.MoldelForm):
    class Meta: 
        model = Pessoa 
        fields = ['nome', 'sobrenome'] 
        