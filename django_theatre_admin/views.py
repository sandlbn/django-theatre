# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from django_theatre.models import Performance, PerformanceTime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.utils.datetime_safe import datetime
from django.views.generic.edit import CreateView, UpdateView,DeleteView, FormMixin
from braces.views import CsrfExemptMixin


class PerformancesView(ListView):
    ''' Performaces List '''
    queryset = Performance.objects.filter().order_by('-id')
    context_object_name = 'performances'
    paginate_by = 20


class PerformanceTimesView(ListView):
    ''' Performaces Time List '''

    context_object_name = 'performances_time'
    paginate_by = 20

    def get_queryset(self, *args, **kwargs):
        self.performance = get_object_or_404(
                            Performance,
                            pk=self.kwargs.get('pk')
                            )
        return PerformanceTime.objects.filter(
                performance=self.performance
                ).order_by('-date')


class PerformanceDeleteView(DeleteView):
    template_name = 'performance_time/performance_time_delete.html'
    model = PerformanceTime
    success_url = '/admin2/performance_time/list/'


class RepertuarCreate(CreateView):
    template_name = 'performance_time/performance_time_create.html'
    model = PerformanceTime
    success_url = '/admin2/performance_time/list/'


class RepertuarUpdate(UpdateView):
    template_name = 'performance_time/performance_time_create_update.html'
    model = PerformanceTime
    success_url = '/admin2/performance_time/list/'
