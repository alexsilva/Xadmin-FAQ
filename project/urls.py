import xadmin
from django.conf.urls import patterns, include, url

xadmin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.index', name='index'),

    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
)
