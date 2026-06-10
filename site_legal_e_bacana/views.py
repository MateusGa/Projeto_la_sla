from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 
from django.urls import reverse_lazy
from datetime import *
from .models import Evento, Subtarefa, Anexo, Lembrete, Usuario, Participante
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView
from django.contrib.auth import logout, update_session_auth_hash
from django.shortcuts import redirect



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


class UsuarioLogin(LoginView):
    template_name = "site_legal_e_bacana/login.html"
    redirect_authenticated_user = True


def usuario_logout(request):
    logout(request)
    return redirect("login")


class UsuarioRegister(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("login")
    extra_context = {
        "titulo": "Cadastro de usuário",
        "botao": "Cadastrar"
    }


class UsuarioPasswordChange(LoginRequiredMixin, FormView):
    template_name = "site_legal_e_bacana/password_change_form.html"
    form_class = SetPasswordForm
    success_url = reverse_lazy("password_change_done")
    login_url = reverse_lazy("login")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class UsuarioPasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = "site_legal_e_bacana/password_change_done.html"
    login_url = reverse_lazy("login")




#_________________________________________________Views para Eventos_________________________________________________#


class EventoCreate(LoginRequiredMixin, CreateView):

    model = Evento
    fields =  ["Evento_nome", "Evento_tipo", "Evento_materia", "Evento_entrega", "Evento_repetir", "Evento_descricao"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Criação de Eventos",
                "botao" : "Criar"

    }


class EventoUpdate(LoginRequiredMixin, UpdateView):

    model = Evento
    fields =  ["Evento_nome", "Evento_tipo", "Evento_materia", "Evento_entrega", "Evento_repetir", "Evento_descricao"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Edição de Eventos",
                "botao" : "Salvar"

    }


class EventoDelete(LoginRequiredMixin, DeleteView):

    model = Evento
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Exclusão de Eventos",
                "botao" : "Excluir para Todo o Sempre"

    }


class EventoList(LoginRequiredMixin, ListView):

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


class EventoDetail(LoginRequiredMixin, DetailView):

    model = Evento
    fields =  ["Evento_nome", "Evento_tipo", "Evento_materia", "Evento_entrega", "Evento_repetir", "Evento_descricao", "Evento_anexos"]
    template_name = "site_legal_e_bacana/ver/eventos.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Olhando Eventos",
                "botao" : "Voltar"

    }





#_________________________________________________Views para Subtarefas_________________________________________________#


class SubtarefaCreate(LoginRequiredMixin, CreateView):

    model = Subtarefa
    fields =  ["Subtarefa_nome", "Subtarefa_concluida", "Subtarefa_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Criação de Subtarefas",
                "botao" : "Criar"

    }


class SubtarefaUpdate(LoginRequiredMixin, UpdateView):

    model = Subtarefa
    fields =  ["Subtarefa_nome", "Subtarefa_concluida", "Subtarefa_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Edição de Subtarefas",
                "botao" : "Salvar"

    }


class SubtarefaDelete(LoginRequiredMixin, DeleteView):

    model = Subtarefa
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Exclusão de Subtarefa",
                "botao" : "Excluir para Todo o Sempre"

    }


class SubtarefaList(LoginRequiredMixin, ListView):

    model = Subtarefa
    template_name = "site_legal_e_bacana/listas/subtarefas.html"


class SubtarefaDetail(LoginRequiredMixin, DetailView):

    model = Subtarefa
    template_name = "site_legal_e_bacana/ver/subtarefas.html"





#_________________________________________________Views para Anexos_________________________________________________#


class AnexoCreate(LoginRequiredMixin, CreateView):

    model = Anexo
    fields =  ["Anexo_nome", "Anexo_arquivo", "Anexo_tamanho", "Anexo_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Criação de Anexos",
                "botao" : "Criar"

    }


class AnexoUpdate(LoginRequiredMixin, UpdateView):

    model = Anexo
    fields =  ["Anexo_nome", "Anexo_arquivo", "Anexo_tamanho", "Anexo_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Edição de Anexos",
                "botao" : "Salvar"

    }


class AnexoDelete(LoginRequiredMixin, DeleteView):

    model = Anexo
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Exclusão de Anexos",
                "botao" : "Excluir para Todo o Sempre"

    }


class AnexoList(LoginRequiredMixin, ListView):

    model = Anexo
    template_name = "site_legal_e_bacana/listas/anexos.html"


class AnexoDetail(LoginRequiredMixin, DetailView):

    model = Anexo
    template_name = "site_legal_e_bacana/ver/anexos.html"




#_________________________________________________Views para Lembretes_________________________________________________#


class LembreteCreate(LoginRequiredMixin, CreateView):

    model = Lembrete
    fields =  ["Lembrete_nome", "Lembrete_date", "Lembrete_desc", "Lembrete_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Criação de Lembretes",
                "botao" : "Criar"

    }


class LembreteUpdate(LoginRequiredMixin, UpdateView):

    model = Lembrete
    fields =  ["Lembrete_nome", "Lembrete_date", "Lembrete_desc", "Lembrete_evento"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Edição de Lembretes",
                "botao" : "Salvar"

    }


class LembreteDelete(LoginRequiredMixin, DeleteView):

    model = Lembrete
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Exclusão de Lembretes",
                "botao" : "Excluir para Todo o Sempre"

    }


class LembreteList(LoginRequiredMixin, ListView):

    model = Lembrete
    template_name = "site_legal_e_bacana/listas/lembretes.html"


class LembreteDetail(LoginRequiredMixin, DetailView):

    model = Lembrete
    template_name = "site_legal_e_bacana/ver/lembretes.html"


#_________________________________________________Views para Participantes_________________________________________________#


class ParticipanteCreate(LoginRequiredMixin, CreateView):

    model = Participante
    fields =  ["Participante_nome", "Participante_email", "Participante_senha"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Adicionar Participantes",
                "botao" : "Adicionar"

    }


class ParticipanteUpdate(LoginRequiredMixin, UpdateView):

    model = Participante
    fields =  ["Participante_nome", "Participante_email", "Participante_senha"]
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Edição de Participantes",
                "botao" : "Salvar"

    }


class ParticipanteDelete(LoginRequiredMixin, DeleteView):

    model = Participante
    template_name = "site_legal_e_bacana/form.html"
    success_url = reverse_lazy("Le_Start")
    extra_context = {
                
                "titulo" : "Exclusão de Participantes",
                "botao" : "Silencia-lo"

    }


class ParticipanteList(LoginRequiredMixin, ListView):

    model = Participante
    template_name = "site_legal_e_bacana/listas/participante.html"


class ParticipanteDetail(LoginRequiredMixin, DetailView):

    model = Participante
    template_name = "site_legal_e_bacana/ver/participante.html"