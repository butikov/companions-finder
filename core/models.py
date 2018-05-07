from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class BasicObjectModel(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    deleted = models.DateTimeField(verbose_name='Дата удаления', editable=False, null=True)


class UGCModel(models.Model):

    class Meta:
        abstract = True

    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), on_delete=models.PROTECT,
                               related_name='user_%(class)s')


class TextModel(models.Model):

    class Meta:
        abstract = True

    text = models.TextField(verbose_name='Текст')
    modified = models.DateTimeField(verbose_name='Изменено', auto_now=True)


class Likable(models.Model):

    class Meta:
        abstract = True

    like_count = models.PositiveIntegerField(verbose_name='Количество лайков', default=0, editable=False)


class ObjectRelatedModel(models.Model):

    class Meta:
        abstract = True
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content = GenericForeignKey(ct_field='content_type', fk_field='object_id')


class Eventable:
    def get_title(self):
        raise NotImplementedError

    def get_author(self):
        raise NotImplementedError

