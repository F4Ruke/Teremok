from django.urls import path
from apps.user.views.login import UserLogIn
from apps.user.views.singup import UserSingUp
from apps.user.views.logout import user_logout

urlpatterns = [
    path('login/', UserLogIn.as_view(), name='login'),
    path('singup/', UserSingUp.as_view(), name='singup'),
    path('logout/', user_logout, name='logout')
]
