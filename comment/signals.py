from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment


@receiver(post_save, sender=Comment)
def save_comment(instance, created=False, **kwargs):
    pass
