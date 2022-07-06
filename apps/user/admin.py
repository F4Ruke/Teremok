from django.contrib import admin
from apps.user.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    """Регистрация модели пользователя в админ-панели"""

    list_display = ('id', 'username', 'first_name', 'last_name', 'phone', 'photo', 'is_active')
