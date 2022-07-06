from django.contrib import admin
from apps.core.models.reservations import Reservations


@admin.register(Reservations)
class ReservationsAdmin(admin.ModelAdmin):
    """Регистрация модели резерваций в админ-панели"""

    list_display = ['id', 'date_check_in', 'date_check_out', 'adult_count',
                    'child_count', 'pet_count', 'advert_id', 'user_id']
