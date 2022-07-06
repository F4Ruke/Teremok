from django.contrib import admin
from apps.core.models.comforts import Comforts


@admin.register(Comforts)
class ComfortsAdmin(admin.ModelAdmin):
    """Регистрация модели удобств в админ-панели"""

    list_display = ['id', 'comfort']
