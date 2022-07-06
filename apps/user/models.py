from django.db import models
from transliterate import translit
from django.contrib.auth.models import AbstractUser
from apps.support import my_awesome_upload_function
from transliterate.exceptions import LanguageDetectionError


class CustomUser(AbstractUser):
    """Модель пользователя"""

    photo = models.FileField(upload_to=my_awesome_upload_function, verbose_name='Путь')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')

    def __str__(self):
        return f"{self.username} - ({self.get_full_name()})"

    def get_directory(self):
        """Возвращает название директории"""

        try:
            dir_name = translit(self.get_full_name(), reversed=True)
        except LanguageDetectionError:
            dir_name = self.get_full_name()

        return str.replace(dir_name, " ", "_")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
