from django.apps import AppConfig


class XPluginConfig(AppConfig):
    name = 'xplugin_mppt'
    verbose_name = "MPTT Plugin"

    def ready(self):
        """"""
