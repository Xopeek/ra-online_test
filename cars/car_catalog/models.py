from django.db import models


class Mark(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Марка'
    )

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Модель',
    )
    mark = models.ForeignKey(
        Mark,
        on_delete=models.CASCADE,
        verbose_name='Марка модели'
    )

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.name
