# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from .views import GalleryBackendListView
from .views import GalleryCreateView
from .views import GalleryUpdateView
from .views import GalleryDeleteView
from .views import PhotoBackendListView
from .views import PhotoCreateView
from .views import PhotoUpdateView
from .views import PhotoDeleteView

from .views import GalleryDetailView

urlpatterns = patterns(
    '.view',
    url(
        r'^gallery,(?P<slug>[\w\d-]+)/$',
        GalleryDetailView.as_view(),
        name='frontend-galery-detail'
    ),
)
urlpatterns += patterns(
    '.views',
    url(
        r'^backend/gallery/list/$',
        GalleryBackendListView.as_view(),
        name='backend-gallery-list'
    ),
    url(
        r'^backend/gallery/create/$',
        GalleryCreateView.as_view(),
        name='backend-gallery-create'
    ),
    url(
        r'^backend/gallery/update/(?P<pk>\d)/$',
        GalleryUpdateView.as_view(),
        name='backend-gallery-update'
    ),
    url(
        r'^backend/gallery/delete/(?P<pk>\d)/$',
        GalleryDeleteView.as_view(),
        name='backend-gallery-delete'
    ),
    url(
        r'^backend/photo/list/(?P<gallery_pk>\d)/$',
        PhotoBackendListView.as_view(),
        name='backend-photo-list'
    ),
    url(
        r'^backend/photo/create/(?P<gallery_pk>\d)/$',
        PhotoCreateView.as_view(),
        name='backend-photo-create'
    ),
    url(
        r'^backend/photo/update/(?P<pk>\d)/$',
        PhotoUpdateView.as_view(),
        name='backend-photo-update'
    ),
    url(
        r'^backend/photo/delete/(?P<pk>\d)/$',
        PhotoDeleteView.as_view(),
        name='backend-photo-delete'
    ),
)
