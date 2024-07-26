from django.views.generic import TemplateView, DetailView

from treemenu.models import Menu

class MenuView(TemplateView):
    template_name = 'treemenu/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

class MenuInfoView(DetailView):
    template_name = 'treemenu/information.html'
    slug_url_kwarg = 'menu_slug'
    context_object_name = ''

    def get_object(self):
        try:
            information = Menu.objects.get(slug = self.kwargs.get(self.slug_url_kwarg))
        except Exception:
            information = Menu.objects.get(named_url = self.kwargs.get(self.slug_url_kwarg))
        return information
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.object.name
        return context