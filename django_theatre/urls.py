# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import patterns, url
from views import FrontPage


urlpatterns = patterns('django_theatre.views',
            url(r'^$', FrontPage.as_view(), name='front_page'),
            )
