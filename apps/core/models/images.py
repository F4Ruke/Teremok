from django.db import models
from transliterate import translit
from apps.core.models.adverts import Adverts
from apps.support import my_awesome_upload_function
from transliterate.exceptions import LanguageDetectionError


class Images(models.Model):
    """Модель картинок объявления"""

    image = models.FileField(upload_to=my_awesome_upload_function, verbose_name="Путь")
    advert_id = models.ForeignKey(Adverts, on_delete=models.CASCADE)

    def get_directory(self):
        """Возвращает название директории"""

        try:
            dir_name = translit(self.advert_id.title, reversed=True)
        except LanguageDetectionError:
            dir_name = self.advert_id.title

        return str.replace(dir_name, " ", "_")

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
