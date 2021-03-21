from django.apps import AppConfig


class AwadsConfig(AppConfig):
    name = 'awads'
    def ready(self):
    	import awads.signals