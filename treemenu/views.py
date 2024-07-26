from django.views.generic import TemplateView

from treemenu.models import Menu

class MenuView(TemplateView):
    template_name = 'treemenu/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
