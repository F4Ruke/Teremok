from django.db import models


class Comforts(models.Model):
    """Модель удобств"""

    comfort = models.CharField(max_length=255, verbose_name="Удобство")

    def __str__(self):
        return self.comfort

    class Meta:
        verbose_name = 'Удобство'
        verbose_name_plural = 'Удобства'
