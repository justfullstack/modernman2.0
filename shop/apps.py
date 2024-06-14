from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

class MainConfig(AppConfig):
    """make sure this file is initialized when the Django application is launched by the internal Django application registry."""
    name = 'main'

    def ready(self):
        from . import signals



