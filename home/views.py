from django.views.generic import TemplateView

class HermesHomePage(TemplateView):
    template_name = 'home/home.html'
