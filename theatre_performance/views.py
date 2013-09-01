# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from .models import Performance
from .models import PerformanceTime
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView
from django.utils.datetime_safe import datetime


class FrontPageView(ListView):
    ''' Start Page with promoted Performances '''
    queryset = PerformanceTime.objects.filter(
        published=True,
        frontpage=True,
        performance_date__gte=datetime.now()
    )
    context_object_name = 'performances'
    template_name = 'index.html'


class PerformanceView(DetailView):
    ''' Single Performance '''
    model = Performance
    slug_field = 'slug'
    context_object_name = 'performances'
    template_name = 'performance.html'


class PerformanceTimeView(DetailView):
    ''' Single Performance Time '''
    model = PerformanceTime
    context_object_name = 'performance'
    template_name = 'performance.html'


class PerformanceMonth(TemplateView):
    ''' Start Page with listed Performances '''

    queryset = PerformanceTime.objects.filter()
    context_object_name = 'performances'
    template_name = 'list.html'
