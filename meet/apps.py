from django.apps import AppConfig


class MeetConfig(AppConfig):
    name = 'meet'

    def ready(self):
        import meet.signals