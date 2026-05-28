from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 
from django.urls import reverse_lazy
from datetime import *
from .models import Evento, Subtarefa, Anexo, Lembrete, Usuario, Participante
from django.contrib.auth.mixins import LoginRequiredMixin



class Index(TemplateView):
    template_name = "site_legal_e_bacana/inicio.html"
    paginate_by = 50



class Sobre(TemplateView):
    template_name = "site_legal_e_bacana/sobre.html"
    paginate_by = 50



class Contato(TemplateView):
    template_name = "site_legal_e_bacana/contatos.html"
    paginate_by = 50
    


class Modelo(TemplateView):
    template_name = "site_legal_e_bacana/modelo.html"
    paginate_by = 50




#_________________________________________________Views para Eventos_________________________________________________#


class EventoCreate(CreateView, LoginRequiredMixin):

    model = Evento
    fields =  ["Evento_nome", "Evento_tipo", "Evento_materia", "Evento_entrega", "Evento_repetir", "Evento_descricao"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Criação de Eventos",
                "botao" : "Criar"

    }


class EventoUpdate(UpdateView, LoginRequiredMixin):

    model = Evento
    fields =  ["Evento_nome", "Evento_tipo", "Evento_materia", "Evento_entrega", "Evento_repetir", "Evento_descricao"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Edição de Eventos",
                "botao" : "Salvar"

    }


class EventoDelete(DeleteView, LoginRequiredMixin):

    model = Evento
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Exclusão de Eventos",
                "botao" : "Excluir para Todo o Sempre"

    }


class EventoList(ListView, LoginRequiredMixin):

    model = Evento
    template_name = "site_legal_e_bacana/listas/eventos.html"

    def get_queryset(self):

        queryset = super().get_queryset().order_by("-Evento_entrega")

        hoje = date.today()

        for evento in queryset:

            evento.dias = (
                evento.Evento_entrega - hoje
            ).days

        return queryset


class EventoDetail(DetailView, LoginRequiredMixin):

    model = Evento
    fields =  ["Evento_nome", "Evento_tipo", "Evento_materia", "Evento_entrega", "Evento_repetir", "Evento_descricao", "Evento_anexos"]
    template_name = "site_legal_e_bacana/ver/eventos.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Olhando Eventos",
                "botao" : "Voltar"

    }





#_________________________________________________Views para Subtarefas_________________________________________________#


class SubtarefaCreate(CreateView, LoginRequiredMixin):

    model = Subtarefa
    fields =  ["Subtarefa_nome", "Subtarefa_concluida", "Subtarefa_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Criação de Subtarefas",
                "botao" : "Criar"

    }


class SubtarefaUpdate(UpdateView, LoginRequiredMixin):

    model = Subtarefa
    fields =  ["Subtarefa_nome", "Subtarefa_concluida", "Subtarefa_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Edição de Subtarefas",
                "botao" : "Salvar"

    }


class SubtarefaDelete(DeleteView, LoginRequiredMixin):

    model = Subtarefa
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Exclusão de Subtarefa",
                "botao" : "Excluir para Todo o Sempre"

    }


class SubtarefaList(ListView, LoginRequiredMixin):

    model = Subtarefa
    template_name = "site_legal_e_bacana/listas/subtarefas.html"


class SubtarefaDetail(DetailView, LoginRequiredMixin):

    model = Subtarefa
    template_name = "site_legal_e_bacana/ver/subtarefas.html"





#_________________________________________________Views para Anexos_________________________________________________#


class AnexoCreate(CreateView, LoginRequiredMixin):

    model = Anexo
    fields =  ["Anexo_nome", "Anexo_arquivo", "Anexo_tamanho", "Anexo_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Criação de Anexos",
                "botao" : "Criar"

    }


class AnexoUpdate(UpdateView, LoginRequiredMixin):

    model = Anexo
    fields =  ["Anexo_nome", "Anexo_arquivo", "Anexo_tamanho", "Anexo_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Edição de Anexos",
                "botao" : "Salvar"

    }


class AnexoDelete(DeleteView, LoginRequiredMixin):

    model = Anexo
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Exclusão de Anexos",
                "botao" : "Excluir para Todo o Sempre"

    }


class AnexoList(ListView, LoginRequiredMixin):

    model = Anexo
    template_name = "site_legal_e_bacana/listas/anexos.html"


class AnexoDetail(DetailView, LoginRequiredMixin):

    model = Anexo
    template_name = "site_legal_e_bacana/ver/anexos.html"




#_________________________________________________Views para Lembretes_________________________________________________#


class LembreteCreate(CreateView, LoginRequiredMixin):

    model = Lembrete
    fields =  ["Lembrete_nome", "Lembrete_date", "Lembrete_desc", "Lembrete_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Criação de Lembretes",
                "botao" : "Criar"

    }


class LembreteUpdate(UpdateView, LoginRequiredMixin):

    model = Lembrete
    fields =  ["Lembrete_nome", "Lembrete_date", "Lembrete_desc", "Lembrete_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Edição de Lembretes",
                "botao" : "Salvar"

    }


class LembreteDelete(DeleteView, LoginRequiredMixin):

    model = Lembrete
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Exclusão de Lembretes",
                "botao" : "Excluir para Todo o Sempre"

    }


class LembreteList(ListView, LoginRequiredMixin):

    model = Lembrete
    template_name = "site_legal_e_bacana/listas/lembretes.html"


class LembreteDetail(DetailView, LoginRequiredMixin):

    model = Lembrete
    template_name = "site_legal_e_bacana/ver/lembretes.html"


#_________________________________________________Views para Participantes_________________________________________________#


class ParticipanteCreate(CreateView, LoginRequiredMixin):

    model = Participante
    fields =  ["Participante_nome", "Participante_email", "Participante_senha"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Adicionar Participantes",
                "botao" : "Adicionar"

    }


class ParticipanteUpdate(UpdateView, LoginRequiredMixin):

    model = Participante
    fields =  ["Participante_nome", "Participante_email", "Participante_senha"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Edição de Participantes",
                "botao" : "Salvar"

    }


class ParticipanteDelete(DeleteView, LoginRequiredMixin):

    model = Participante
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Exclusão de Participantes",
                "botao" : "Silencia-lo"

    }


class ParticipanteList(ListView, LoginRequiredMixin):

    model = Participante
    template_name = "site_legal_e_bacana/listas/participante.html"


class ParticipanteDetail(DetailView, LoginRequiredMixin):

    model = Participante
    template_name = "site_legal_e_bacana/ver/participante.html"