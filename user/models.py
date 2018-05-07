from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class DefaultUser(AbstractUser):

    subscriptions = models.ManyToManyField(to='self', verbose_name='Подписки',
                                           related_name='subscribers')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
