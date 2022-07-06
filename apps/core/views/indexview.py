from django.views.generic import ListView
from apps.core.models.adverts import Adverts


class IndexView(ListView):
    """Главная страница"""

    model = Adverts
    template_name = 'core/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Главная'

        return context
