from django.db import models


class Category(models.Model):
    title = models.SlugField(verbose_name='Название', unique=True, primary_key=True, max_length=127)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
