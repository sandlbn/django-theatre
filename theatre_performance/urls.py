# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from .views import FrontPageView
from .views import PerformanceView
from .views import PerformanceList
from .views import PerformanceBackendListView
from .views import PerformanceCreateView
from .views import PerformanceUpdateView
from .views import PerformanceDeleteView
from .views import PerformanceGenreBackendListView
from .views import PerformanceGenreCreateView
from .views import PerformanceGenreUpdateView
from .views import PerformanceGenreDeleteView

urlpatterns = patterns(
    '.views',
    url(
        r'^backend/performance/list/$',
        PerformanceBackendListView.as_view(),
        name='backend-performance-list'
    ),
    url(
        r'^backend/performance/create/$',
        PerformanceCreateView.as_view(),
        name='backend-performance-create'
    ),
    url(
        r'^backend/performance/update/(?P<pk>\d)/$',
        PerformanceUpdateView.as_view(),
        name='backend-performance-update'
    ),
    url(
        r'^backend/performance/delete/(?P<pk>\d)/$',
        PerformanceDeleteView.as_view(),
        name='backend-performance-delete'
    ),
    url(
        r'^backend/performancegenre/list/$',
        PerformanceGenreBackendListView.as_view(),
        name='backend-performance-genre-list'
    ),
    url(
        r'^backend/performancegenre/create/$',
        PerformanceGenreCreateView.as_view(),
        name='backend-performance-genre-create'
    ),
    url(
        r'^backend/performancegenre/update/(?P<pk>\d)/$',
        PerformanceGenreUpdateView.as_view(),
        name='backend-performance-genre-update'
    ),
    url(
        r'^backend/performancegenre/delete/(?P<pk>\d)/$',
        PerformanceGenreDeleteView.as_view(),
        name='backend-performance-genre-delete'
    ),
)
