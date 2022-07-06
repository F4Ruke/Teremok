from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from apps.user.forms.singup import *
from django.views.generic import CreateView


class UserSingUp(CreateView):
    """Регистрация пользователя"""
    form_class = SingupForm
    template_name = 'user/singup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)

        form = SingupForm()

        contex['title'] = 'Регистрация'
        contex['form'] = form

        return contex

    def form_valid(self, form):
        """Авторизация при успешной регистрации"""
        user = form.save()
        login(self.request, user)
        return redirect('index')
