# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from models import Performance, PerformanceTime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponse
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
    template_name = 'performance.html'
