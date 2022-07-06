from django.views.generic import ListView
from apps.core.models.adverts import Adverts


class AdvertsView(ListView):
    """Страница с объявлениями"""

    model = Adverts
    template_name = 'core/adverts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Объявления'
        context['adverts'] = Adverts.objects.all()

        return context
