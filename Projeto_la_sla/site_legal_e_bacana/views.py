from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "site_legal_e_bacana/inicio.html"

class Sobre(TemplateView):
    template_name = "site_legal_e_bacana/sobre.html"

class Contato(TemplateView):
    template_name = "site_legal_e_bacana/contatos.html"