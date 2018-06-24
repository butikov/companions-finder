from core import models
from django.db import models as fields
from django.contrib.auth import get_user_model
from category.models import Category
from django.contrib.gis.db.models import PointField


class Meet(models.BasicObjectModel, models.UGCModel, models.TextModel, models.Likable):

    title = fields.CharField(verbose_name='Название', max_length=255)
    participants = fields.ManyToManyField(verbose_name='Участники', to=get_user_model(),
                                          related_name='participated_meets', blank=True)
    meet_time = fields.DateTimeField(verbose_name='Время проведения')
    max_participants = fields.PositiveIntegerField(verbose_name='Максимальное кол-во участников', default=0)
    coordinates = PointField(verbose_name='Координаты')
    categories = fields.ManyToManyField(to=Category, verbose_name='Категории', related_name='meets')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    # @fields.permalink
    # def get_absolute_url(self):
    #     return "api/v1/meet/" + str(self.pk)

    def __str__(self):
        return self.title
