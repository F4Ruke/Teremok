from django.db import models
from apps.user.models import CustomUser
from apps.core.models.comforts import Comforts


class Adverts(models.Model):
    """Модель объявления"""

    CATEGORY_CHOICES = (
        ('Дом', 'Дом'),
        ('Студия', 'Студия'),
        ('Квартира', 'Квартира'),
        ('Лофт', 'Лофт'),
        ('Коттедж', 'Коттедж'),
        ('Вилла', 'Вилла'),
        ('Дуплекс', 'Дуплекс'),
        ('Таунхаус', 'Таунхаус'),
        ('Пентхаус', 'Пентхаус'),
        ('Апартаменты', 'Апартаменты'),
    )

    title = models.CharField(max_length=64, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES, verbose_name="Тип жилья")
    city = models.CharField(max_length=64, verbose_name="Город")
    street = models.CharField(max_length=64, verbose_name="Улица")
    home_number = models.CharField(max_length=8, verbose_name="Номер дома")
    guest_count = models.IntegerField(verbose_name="Кол-во гостей")
    bed_count = models.IntegerField(verbose_name="Кол-во кроватей")
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Цена")
    comfort = models.ManyToManyField(Comforts, verbose_name="Удобства")
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
