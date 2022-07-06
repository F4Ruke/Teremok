from apps.user.forms.login import LoginForm
from django.contrib.auth.views import LoginView


class UserLogIn(LoginView):
    """Авторизация пользователя"""

    form_class = LoginForm
    template_name = 'user/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)

        contex['title'] = 'Авторизация'

        return contex
