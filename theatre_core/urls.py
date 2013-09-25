# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from .views import DonorBackendListView
from .views import DonorCreateView
from .views import DonorUpdateView
from .views import DonorDeleteView

urlpatterns = patterns(
    '.views',
    url(
        r'^backend/donor/list/$',
        DonorBackendListView.as_view(),
        name='backend-donor-list'
    ),
    url(
        r'^backend/donor/create/$',
        DonorCreateView.as_view(),
        name='backend-donor-create'
    ),
    url(
        r'^backend/donor/update/(?P<pk>\d+)/$',
        DonorUpdateView.as_view(),
        name='backend-donor-update'
    ),
    url(
        r'^backend/donor/delete/(?P<pk>\d+)/$',
        DonorDeleteView.as_view(),
        name='backend-donor-delete'
    ),
)
