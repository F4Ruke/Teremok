from django.contrib import admin
from apps.core.models.reviews import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Регистрация модели отзывов в админ-панели"""

    list_display = ['id', 'review', 'advert_id', 'user_id']
