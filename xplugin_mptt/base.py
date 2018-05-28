# coding:utf-8
# author 'sai'
import xadmin
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from xadmin.views import LoginView, BaseAdminView, BaseAdminPlugin, ListAdminView

User = get_user_model()


# 列表点击进入Detail
class ListDetailPlugin(BaseAdminPlugin):
    ListDetail = True

    def init_request(self, *args, **kwargs):
        return bool(self.ListDetail)

    def url_for_result(self, __, *args, **kwargs):
        return self.get_model_url(self.model, 'detail', args[0].pk)


xadmin.site.register_plugin(ListDetailPlugin, ListAdminView)


class AnonymousUserPlugin(BaseAdminPlugin):
    def init_request(self, *args, **kwargs):
        if not self.request.user.pk:
            user = authenticate(username='AnonymousUser', password='admin')
            login(self.request, user)


xadmin.site.register_plugin(AnonymousUserPlugin, BaseAdminView)


class UserLoginPlugin(BaseAdminPlugin):
    def update_params(self, __, defaults):
        new_context = {
            REDIRECT_FIELD_NAME: self.get_admin_url('index'),
        }
        defaults['extra_context'].update(new_context)
        return defaults


xadmin.site.register_plugin(UserLoginPlugin, LoginView)
