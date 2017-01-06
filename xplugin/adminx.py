# coding:utf-8
import xadmin
from xadmin import site
from xadmin.views import ListAdminView
from xadmin.views import ModelFormAdminView

from xplugin.mptree import MPTTListPlugin, MPTTFormPlugin


class GolbeSetting(object):
    # menu_style = 'accordion'
    site_title = u'Xadmin FAQ'
    base_template = 'faq_base_site.html'


site.register(xadmin.views.CommAdminView, GolbeSetting)

site.register_plugin(MPTTListPlugin, ListAdminView)
site.register_plugin(MPTTFormPlugin, ModelFormAdminView)