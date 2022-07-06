from django.contrib import admin
from apps.core.models.adverts import Adverts


@admin.register(Adverts)
class AdvertsAdmin(admin.ModelAdmin):
    """Регистрация модели объявлений в админ-панели"""

    list_display = ['id', 'title', 'description', 'city', 'street', 'home_number', 'guest_count',
                    'bed_count', 'price', 'user_id']
