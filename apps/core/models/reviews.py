from django.db import models
from apps.user.models import CustomUser
from apps.core.models.adverts import Adverts


class Reviews(models.Model):
    """Модель отзывов объявления"""

    review = models.TextField(verbose_name="Комментарий")
    advert_id = models.ForeignKey(Adverts, on_delete=models.CASCADE, verbose_name="Объявление")
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return self.review

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
