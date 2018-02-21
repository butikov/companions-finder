from django.db import models


class Category(models.Model):
    title = models.SlugField()
