from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class Usuario(models.Model):

    Usuario_nome = models.CharField(max_length=50, verbose_name='Seu 🫵 nome')
    Usuario_email = models.EmailField(max_length=254, verbose_name='Seu E-mail')
    Usuario_senha = models.CharField(max_length=30, verbose_name='Seu nome')

    def __str__(self):
        return f"{self.Usuario_nome}"


class Evento(models.Model):

    Evento_nome = models.CharField(max_length=50)
    Evento_tipo = models.CharField(max_length=50)
    Evento_materia = models.CharField(max_length=50)
    Evento_entrega = models.DateField()
    Evento_repetir = models.BooleanField()
    Evento_descricao = models.TextField(verbose_name="Descrição")
    
    #tem que fazer com url


    #Evento_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.Evento_nome}"
    
    
class Subtarefa(models.Model):

    Subtarefa_nome = models.CharField(max_length=50)
    Subtarefa_concluida = models.BooleanField()

    Subtarefa_evento = models.ForeignKey(Evento, on_delete=models.CASCADE, verbose_name="Evento")

    def __str__(self):

        if self.Subtarefa_concluida:
            return (f"{self.Subtarefa_nome} - Concluído 👍👍👍")
        else:
            return (f"{self.Subtarefa_nome} - Não Concluído 👎👎👎")


class Anexo(models.Model):

    Anexo_nome = models.CharField(max_length=50, verbose_name='Nome do Anexo')
    Anexo_arquivo = models.CharField(verbose_name='Arquivo')
    Anexo_tamanho = models.PositiveIntegerField(verbose_name='Tamanho do Arquivo')

    Anexo_evento = models.ForeignKey(Evento, on_delete=models.CASCADE, verbose_name="Evento")
    
    def __str__(self):
        return f"{self.Anexo_nome}"


class Lembrete(models.Model):

    Lembrete_nome = models.CharField(max_length=50, verbose_name='Nome do lembrete')
    Lembrete_date = models.DateField(verbose_name='Data do lembrete')
    Lembrete_desc = models.TextField(max_length=250, verbose_name='Descrição', blank=True, default='Eu sou uma descrição padrão. Ha')

    Lembrete_evento = models.ForeignKey(Evento, on_delete=models.CASCADE, verbose_name="Evento")

    def __str__(self):
        return f"{self.Lembrete_nome}"

class Participante(models.Model):

    Participante_nome = models.CharField(max_length=50, verbose_name='Nome dele')
    Participante_email = models.EmailField(max_length=254, verbose_name='E-mail dele')
    Participante_senha = models.CharField(max_length=30, verbose_name='Senha dele')

    def __str__(self):
        return f"{self.Participante_nome}"
