from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    # def ready(self): #method just to import the signals
    # 	import core.signals