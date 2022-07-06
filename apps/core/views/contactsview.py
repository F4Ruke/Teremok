from django.views.generic import ListView
from apps.core.models.adverts import Adverts


class ContactsView(ListView):
    """Страница Контакты"""

    model = Adverts
    template_name = 'core/contacts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Контакты'

        return context
