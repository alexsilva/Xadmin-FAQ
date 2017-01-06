from django.apps import AppConfig


class XPluginConfig(AppConfig):
    name = 'xplugin'
    verbose_name = "MPTT Plugin"

    def ready(self):
        """"""
