# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    #设置文章相关URL
    url(r'^(?P<id>[^/]+)/$','article.views.article',name='article'),
    url(r'^(?P<cid>[^/]+)/(?P<id>[^/]+)/$','article.views.article_show',name='article_show'),
)
