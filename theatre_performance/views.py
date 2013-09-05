# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from .models import Performance
from .models import PerformanceTime
from .forms import PerformanceForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.utils.datetime_safe import datetime
from braces.views import StaffuserRequiredMixin
from django.core.urlresolvers import reverse_lazy


class FrontPageView(ListView):
    ''' Start Page with promoted Performances '''
    queryset = PerformanceTime.objects.filter(
        published=True,
        frontpage=True,
        performance_date__gte=datetime.now()
    )
    template_name = 'index.html'


class PerformanceView(DetailView):
    ''' Single Performance '''
    model = Performance
    slug_field = 'slug'
    template_name = 'performance.html'


class PerformanceTimeView(DetailView):
    ''' Single Performance Time '''
    model = PerformanceTime
    context_object_name = 'performance'
    template_name = 'performance_time_detail.html'


class PerformanceList(ListView):
    ''' Start Page with listed Performances '''

    queryset = PerformanceTime.objects.filter(
        published=True,
    )
    template_name = 'theatre_performance/performance_list_calendar.html'


class PerformanceBackendList(ListView):
    ''' Start Page with listed Performances '''

    model = Performance
    template_name = 'theatre_performance/backend/performance_list.html'


class PerformanceCreateView(CreateView, StaffuserRequiredMixin):

    model = Performance
    form_class = PerformanceForm
    success_url = reverse_lazy('backend-performance-list')
    template_name = 'theatre_performance/backend/performance_create_form.html'


class PerformanceUpdateView(UpdateView, StaffuserRequiredMixin):

    model = Performance
    form_class = PerformanceForm
    success_url = reverse_lazy('backend-performance-list')
    template_name = 'theatre_performance/backend/performance_update_form.html'


class PerformanceDeleteView(DeleteView, StaffuserRequiredMixin):

    model = Performance
    success_url = reverse_lazy('backend-performance-list')
    template_name = 'theatre_performance/backend/performance_confirm_delete.html'


class PerformanceListBackendView(ListView, StaffuserRequiredMixin):

    model = Performance
    template_name = 'theatre_performance/backend/performance_list.html'
