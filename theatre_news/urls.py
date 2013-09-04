
# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from .views import NewsDetailView
from .views import StaticPageDetailView
from .views import NewsCreateView
from .views import NewsUpdateView
from .views import NewsDeleteView
from .views import NewsListBackendView
from .views import StaticPageCreateView
from .views import StaticPageUpdateView
from .views import StaticPageDeleteView
from .views import StaticPageListView


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
        name='static-detail'
    )
)

urlpatterns += patterns(
    '.views',
    url(
        r'^backend/static/list/$',
        StaticPageListView.as_view(),
        name='backend-static-list'
    ),
    url(
        r'^backend/static/create/$',
        StaticPageCreateView.as_view(),
        name='backend-static-create'
    ),
    url(
        r'^backend/static/update/(?P<pk>\d)/$',
        StaticPageUpdateView.as_view(),
        name='backend-static-update'
    ),
    url(
        r'^backend/static/delete/(?P<pk>\d)/$',
        StaticPageDeleteView.as_view(),
        name='backend-static-delete'
    ),
    url(
        r'^backend/news/list/$',
        NewsListBackendView.as_view(),
        name='backend-news-list'
    ),
    url(
        r'^backend/news/create/$',
        NewsCreateView.as_view(),
        name='backend-news-create'
    ),
    url(
        r'^backend/news/update/(?P<pk>\d)/$',
        NewsUpdateView.as_view(),
        name='backend-news-update'
    ),
    url(
        r'^backend/news/delete/(?P<pk>\d)/$',
        NewsDeleteView.as_view(),
        name='backend-news-delete'
    ),
)

