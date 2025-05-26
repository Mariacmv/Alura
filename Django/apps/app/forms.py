from django import forms
from apps.app.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta: #diz respeito aos metadados da minha classe
        model = Fotografia #digo para qual model estou me referindo
        
        exclude = ['publicada',] #lista para as fotos que não quero que apareçam porque estou me baseando no meu models.py da class fotografia
        labels = { #defino como quero que apareça para o usuário
            'descricao':'Descrição',
            'data_fotografia':'Data de registro',
            'usuario':'Usuário',
        }
        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'legenda':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'descricao':forms.Textarea(attrs={'class':'form-control'}),
            'foto':forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia':forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'class':'form-control',
                    'type':'date'
                }
            ),
            'usuario':forms.Select(attrs={'class':'form-control'}),
        } #quais classe do css devem operar