from django.apps import AppConfig


class DblearningConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dblearning"

class UserAppConfig(AppConfig):
    name = 'dblearning'

    def ready(self):
        import dblearning.signals