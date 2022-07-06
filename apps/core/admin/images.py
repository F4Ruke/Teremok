from django.contrib import admin
from apps.core.models.images import Images


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    """Регистрация модели картинок в админ-панели"""

    list_display = ['id', 'image', 'advert_id']
