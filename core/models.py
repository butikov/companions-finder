from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser


class BasicObjectModel(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_created=True)
    is_deleted = models.BooleanField(default=False)


class UGCModel(BasicObjectModel):

    class Meta:
        abstract = True

    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='user_%(class)s')


class TextModel(UGCModel):

    class Meta:
        abstract = True

    text = models.TextField()
    modified = models.DateTimeField(auto_now_add=True)


class ObjectRelatedModel(models.Model):

    class Meta:
        abstract = True
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content = GenericForeignKey(ct_field='content_type', fk_field='object_id')


class User(AbstractUser):

    subscriptions = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribers')
