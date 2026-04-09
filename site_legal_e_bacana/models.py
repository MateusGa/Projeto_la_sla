from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Ususario(models.Model):

    Usuario_nome = models.CharField(max_length=50, verbose_name='Seu 🫵 nome')
    Usuario_email = models.EmailField(max_length=254, verbose_name='Seu E-mail')
    Usuario_senha = models.CharField(max_length=30, verbose_name='Seu nome')

    def __str__(self):
        return self.Usuario_nome


class Evento(models.Model):

    Evento_nome = models.CharField(max_length=50)
    Evento_tipo = models.CharField(max_length=50)
    Evento_materia = models.CharField(max_length=50)
    Evento_entrega = models.DateField()
    Evento_repetir = models.BooleanField()

    Evento_usuario = models.ForeignKey(Ususario, on_delete=models.CASCADE)

    def __str__(self):
        return self.Evento_nome
    
    
class Subtarefa(models.Model):

    Subtarefa_nome = models.CharField(max_length=50)
    Subtarefa_concluida = models.BooleanField()

    Subtarefa_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.Subtarefa_nome


class Anexo(models.Model):

    Anexo_nome = models.CharField(max_length=50, verbose_name='Nome do Anexo')
    Anexo_arquivo = models.FileField(verbose_name='Arquivo')
    Anexo_tamanho = models.PositiveIntegerField(verbose_name='Tamanho do Arquivo')

    Anexo_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Anexo_nome


class Lembrete(models.Model):

    Lembrete_nome = models.CharField(max_length=50, verbose_name='Nome do lembrete')
    Lembrete_date = models.DateField(verbose_name='Data do lembrete')
    Lembrete_desc = models.TextField(max_length=250, verbose_name='Descrição', blank=True, default='Eu sou uma descrição padrão. Ha')

    Lembrete_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.Lembrete_nome

