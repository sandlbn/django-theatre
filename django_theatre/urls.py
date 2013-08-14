# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from views import FrontPageView, PerformanceView


urlpatterns = patterns('django_theatre.views',
            url(r'^$', FrontPageView.as_view(), name='front_page'),
            url(
                r'^performance,(?P<slug>[\w\d-]+)/$',
                PerformanceView.as_view(),
                name='performance'),
            )
