# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from .models import Performance
from .models import PerformanceFrontPage
from .models import PerformanceGenre
from .models import PerformanceTime
from .models import PerformanceDonor
from theatre_news.models import News
from .forms import PerformanceForm
from .forms import PerformanceTimeForm
from .forms import PerformanceDonorForm
from .forms import PerformanceGenreForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView
from django.utils.datetime_safe import datetime
from braces.views import StaffuserRequiredMixin
from django.core.urlresolvers import reverse_lazy
from theatre_core.utils.path import template_path


class FrontPageView(ListView):
    ''' Start Page with promoted Performances '''
    queryset = PerformanceFrontPage.objects.filter(
    )

    def get_context_data(self, *args, **kwargs):

        context = super(FrontPageView, self).get_context_data(**kwargs)
        context["performances"] = self.queryset
        context['news'] = News.objects.filter(
            published=True).order_by('-id')[:3]
        return context
    template_name = template_path(PerformanceTime, 'frontend', 'index')


class PerformanceView(DetailView):
    ''' Single Performance '''
    model = Performance
    slug_field = 'slug'
    template_name = 'performance.html'


class PerformanceTimeDetailView(DetailView):
    ''' Single Performance Time '''
    model = PerformanceTime
    context_object_name = 'performance'
    template_name = template_path(PerformanceTime, 'frontend', 'detail')


class PerformanceList(TemplateView):
    ''' Start Page with listed Performances '''

    template_name = template_path(Performance, 'frontend', 'time_calendar')


class PerformanceBackendListView(ListView):
    ''' Start Page with listed Performances '''

    model = Performance
    template_name = template_path(Performance, 'backend', 'list')


class PerformanceCreateView(CreateView, StaffuserRequiredMixin):

    model = Performance
    form_class = PerformanceForm
    success_url = reverse_lazy('backend-performance-list')
    template_name = template_path(Performance, 'backend', 'create_form')


class PerformanceUpdateView(UpdateView, StaffuserRequiredMixin):

    model = Performance
    form_class = PerformanceForm
    success_url = reverse_lazy('backend-performance-list')
    template_name = template_path(Performance, 'backend', 'update_form')


class PerformanceDeleteView(DeleteView, StaffuserRequiredMixin):

    model = Performance
    success_url = reverse_lazy('backend-performance-list')
    template_name = template_path(Performance, 'backend', 'confirm_delete')


class PerformanceGenreBackendListView(ListView):
    ''' Start Page with listed Performances '''

    model = PerformanceGenre
    template_name = template_path(PerformanceGenre, 'backend', 'list')


class PerformanceGenreCreateView(CreateView, StaffuserRequiredMixin):

    model = PerformanceGenre
    form_class = PerformanceGenreForm
    success_url = reverse_lazy('backend-performance-genre-list')
    template_name = template_path(PerformanceGenre, 'backend', 'create_form')


class PerformanceGenreUpdateView(UpdateView, StaffuserRequiredMixin):

    model = PerformanceGenre
    form_class = PerformanceGenreForm
    success_url = reverse_lazy('backend-performance-genre-list')
    template_name = template_path(PerformanceGenre, 'backend', 'update_form')


class PerformanceGenreDeleteView(DeleteView, StaffuserRequiredMixin):

    model = PerformanceGenre
    success_url = reverse_lazy('backend-performance-genre-list')
    template_name = template_path(PerformanceGenre, 'backend',
                                  'confirm_delete')


class PerformanceTimeBackendListView(ListView):
    ''' Start Page with listed Performances '''

    model = PerformanceTime
    template_name = template_path(PerformanceTime, 'backend', 'list')


class PerformanceTimeCreateView(CreateView, StaffuserRequiredMixin):

    model = PerformanceTime
    form_class = PerformanceTimeForm
    success_url = reverse_lazy('backend-performance-time-list')
    template_name = template_path(PerformanceTime, 'backend', 'create_form')


class PerformanceTimeUpdateView(UpdateView, StaffuserRequiredMixin):

    model = PerformanceTime
    form_class = PerformanceTimeForm
    success_url = reverse_lazy('backend-performance-time-list')
    template_name = template_path(PerformanceTime, 'backend', 'update_form')


class PerformanceTimeDeleteView(DeleteView, StaffuserRequiredMixin):

    model = PerformanceTime
    success_url = reverse_lazy('backend-performance-time-list')
    template_name = template_path(PerformanceTime, 'backend', 'confirm_delete')


class PerformanceDonorBackendListView(ListView):
    ''' Start Page with listed Performance Donor '''

    model = PerformanceDonor
    template_name = template_path(PerformanceDonor, 'backend', 'list')


class PerformanceDonorCreateView(CreateView, StaffuserRequiredMixin):

    model = PerformanceDonor
    form_class = PerformanceDonorForm
    success_url = reverse_lazy('backend-performance-donor-list')
    template_name = template_path(PerformanceDonor, 'backend', 'create_form')


class PerformanceDonorUpdateView(UpdateView, StaffuserRequiredMixin):

    model = PerformanceDonor
    form_class = PerformanceDonorForm
    success_url = reverse_lazy('backend-performance-donor-list')
    template_name = template_path(PerformanceDonor, 'backend', 'update_form')


class PerformanceDonorDeleteView(DeleteView, StaffuserRequiredMixin):

    model = PerformanceTime
    success_url = reverse_lazy('backend-performance-donor-list')
    template_name = template_path(PerformanceDonor, 'backend',
                                  'confirm_delete')
