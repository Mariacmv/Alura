from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Fotografia(models.Model): #herda a biblioteca
    
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]#lista de tuplas porque charfield só entende tuplas
    
    nome = models.CharField(max_length=100, null=False, blank=False) #nome será uma string e defino a quantidade de caracteres que os nomes podem assumir. Não pode não ter informação e não pode conter string vazia
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False) #textfield porque é maior
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True) #para o usuário adicionar itens ao site. É padrão false
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)#incrementando a data de adição
    usuario = models.ForeignKey(
        to = User, #associei à tabela de usuário
        on_delete = models.SET_NULL,#quando o usuário for deletado
        null = True, #ou seja, um usuário pode ser vazio
        blank = False, 
        related_name = "user", #pra localizar a tabela 
    )
    
    #uma boa prática é devolver o nome de cada um dos itens através de uma função
    def __str__(self):
        return self.nome
    

