from core.models import TextModel
from django.db import models
from django.conf import settings
from category.models import Category
from django.contrib.gis.db.models import PointField


class Event(TextModel):

    title = models.CharField(max_length=255)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    event_time = models.DateTimeField()
    max_participants = models.IntegerField(default=0)
    coordinates = PointField()
    categories = models.ManyToManyField(Category, related_name='events')
