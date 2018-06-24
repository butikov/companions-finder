from celery import task
from templated_email import send_templated_mail
from django.contrib.auth import get_user_model


@task
def send_activation_email(self, user_id):
    user = get_user_model().objects.get(user_id)
    try:
        send_templated_mail('activation', 'admin@lh.ru', [user.email, ], context={'user': user})
    except Exception as ex:
        raise self.retry(exc=ex, countdown=60)
