from django.db import models
from apps.user.models import CustomUser
from apps.core.models.adverts import Adverts


class Reservations(models.Model):
    """Модель резервации объявления"""

    date_check_in = models.DateField(verbose_name="Дата заезда")
    date_check_out = models.DateField(verbose_name="Дата выезда")
    adult_count = models.IntegerField(verbose_name="Кол-во гостей")
    child_count = models.IntegerField(verbose_name="Кол-во детей")
    pet_count = models.IntegerField(verbose_name="Кол-во питомцев")
    advert_id = models.ForeignKey(Adverts, on_delete=models.CASCADE, verbose_name="Объявление")
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")

    class Meta:
        verbose_name = 'Резервация'
        verbose_name_plural = 'Резервации'
