from django.apps import AppConfig


class ShopConfig(AppConfig): 
    """make sure this file is initialized when the Django application is launched by the internal Django application registry."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

    def ready(self):
        from . import signals



