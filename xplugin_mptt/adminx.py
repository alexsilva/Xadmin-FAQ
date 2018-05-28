# coding:utf-8
import xadmin
from django.conf import settings
from xadmin import site
from xadmin.views import ListAdminView
from xadmin.views import ModelFormAdminView

from .mptree import MPTTListPlugin, MPTTFormPlugin


class GolbeSetting(object):
    # menu_style = 'accordion'
    site_title = u'Xadmin FAQ'
    base_template = 'faq_base_site.html'


if getattr(settings, "XADMIN_MPTT_PLUGIN_GLOBAL_SETTINGS", False):
    site.register(xadmin.views.CommAdminView, GolbeSetting)

site.register_plugin(MPTTListPlugin, ListAdminView)
site.register_plugin(MPTTFormPlugin, ModelFormAdminView)
