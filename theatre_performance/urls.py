# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from .views import FrontPageView
from .views import PerformanceTimeDetailView
from .views import PerformanceList
from .views import PerformanceBackendListView
from .views import PerformanceCreateView
from .views import PerformanceUpdateView
from .views import PerformanceDeleteView
from .views import PerformanceGenreBackendListView
from .views import PerformanceGenreCreateView
from .views import PerformanceGenreUpdateView
from .views import PerformanceGenreDeleteView
from .views import PerformanceTimeBackendListView
from .views import PerformanceTimeCreateView
from .views import PerformanceTimeUpdateView
from .views import PerformanceTimeDeleteView
from .views import PerformanceDonorBackendListView
from .views import PerformanceDonorCreateView
from .views import PerformanceDonorUpdateView
from .views import PerformanceDonorDeleteView


urlpatterns = patterns(
    '.views',
    url(
        r'^performance,(?P<slug>[\w\d-]+)$',
        PerformanceTimeDetailView.as_view(),
        name='frontend-performance-time-detail'
    ),
)

"""
Duplicated for a default view in backend
"""
urlpatterns += patterns(
    '.views',
    url(
        r'^backend/performance/list/$',
        PerformanceBackendListView.as_view(),
        name='backend-performance-list'
    ),
    url(
        r'^backend/$',
        PerformanceBackendListView.as_view(),
        name='backend-default'
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
    url(
        r'^backend/performancetime/list/$',
        PerformanceTimeBackendListView.as_view(),
        name='backend-performance-time-list'
    ),
    url(
        r'^backend/performancetime/list/(?P<performance_pk>\d)/$',
        PerformanceTimeBackendListView.as_view(),
        name='backend-performance-time-list-filtered'
    ),
    url(
        r'^backend/performancetime/create/$',
        PerformanceTimeCreateView.as_view(),
        name='backend-performance-time-create'
    ),
    url(
        r'^backend/performancetime/update/(?P<pk>\d)/$',
        PerformanceTimeUpdateView.as_view(),
        name='backend-performance-time-update'
    ),
    url(
        r'^backend/performancetime/delete/(?P<pk>\d)/$',
        PerformanceTimeDeleteView.as_view(),
        name='backend-performance-time-delete'
    ),
    url(
        r'^backend/performancedonor/list/$',
        PerformanceDonorBackendListView.as_view(),
        name='backend-performance-donor-list'
    ),
    url(
        r'^backend/performancedonor/create/$',
        PerformanceDonorCreateView.as_view(),
        name='backend-performance-donor-create'
    ),
    url(
        r'^backend/performancedonor/update/(?P<pk>\d)/$',
        PerformanceDonorUpdateView.as_view(),
        name='backend-performance-donor-update'
    ),
    url(
        r'^backend/performancedonor/delete/(?P<pk>\d)/$',
        PerformanceDonorDeleteView.as_view(),
        name='backend-performance-donor-delete'
    ),
)
