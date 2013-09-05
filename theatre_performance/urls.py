# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from .views import FrontPageView
from .views import PerformanceView
from .views import PerformanceList
from .views import PerformanceBackendList
from .views import PerformanceMonth
from .views import PerformanceCreateView
from .views import PerformanceUpdateView
from .views import PerformanceDeleteView

urlatterns += patterns(
    '.views',
    url(
        r'^backend/performance/list/$',
        PerformanceBackendListView.as_view(),
        name='backend-performance-list'
    ),
    url(
        r'^backend/static/create/$',
        PerformanceCreateView.as_view(),
        name='backend-static-create'
    ),
    url(
        r'^backend/static/update/(?P<pk>\d)/$',
        PerformanceUpdateView.as_view(),
        name='backend-static-update'
    ),
    url(
        r'^backend/static/delete/(?P<pk>\d)/$',
        PerformanceDeleteView.as_view(),
        name='backend-static-delete'
    ),
)
