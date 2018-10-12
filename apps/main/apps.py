from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'apps.main'
    verbose_name = 'Main'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import signals  # noqa
