from django.shortcuts import redirect
from django.contrib.auth import logout


def user_logout(request):
    """Выход из аккаунта"""

    logout(request)
    return redirect('index')
