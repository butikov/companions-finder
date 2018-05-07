from django.db.models.signals import post_save, pre_save
from django.db.models import F
from django.dispatch import receiver
from .models import Meet


@receiver(post_save, sender=Meet)
def add_author_to_participants(instance, created=False, **kwargs):
    if created:
        instance.participants.add(instance.author)
