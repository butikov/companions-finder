from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
git

class BasicObjectModel(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_created=True)
    is_deleted = models.BooleanField(default=False)


class UGCModel(BasicObjectModel):

    class Meta:
        abstract = True

    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='actions')


class TextModel(UGCModel):

    class Meta:
        abstract = True

    text = models.TextField()
    modified = models.DateTimeField(auto_now_add=True)


class ObjectRelatedModel(UGCModel):

    class Meta:
        abstract = True

    content = models.ForeignKey(to=BasicObjectModel, on_delete=models.PROTECT)


class User(AbstractUser):

    subscriptions = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribers')
