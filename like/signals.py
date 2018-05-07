from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Like


@receiver(post_save, sender=Like)
def like_added(instance, **kwargs):
    pass


@receiver(post_delete, sender=Like)
def like_deleted(instance, **kwargs):
    pass
