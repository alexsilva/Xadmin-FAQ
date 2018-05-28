from django.apps import AppConfig


class XPluginConfig(AppConfig):
    name = 'xplugin_mptt'
    verbose_name = "MPTT Plugin"

    def ready(self):
        """"""
