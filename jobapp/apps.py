from django.apps import AppConfig


class JobappConfig(AppConfig):
    name = 'jobapp'


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_app'