
# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from .views import NewsDetailView
from .views import StaticPageDetailView


urlpatterns = patterns(
    '.views',
    url(
        r'^news,(?P<slug>[\w\d-]+)/$',
        NewsDetailView.as_view(),
        name='news-detail'
    ),
    url(
        r'^page,(?P<slug>[\w\d-]+)/$',
        StaticPageDetailView.as_view(),
        name='news-detail'
    )
)
