# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from .models import Donor
from .forms import DonorForm
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from braces.views import StaffuserRequiredMixin
from django.core.urlresolvers import reverse_lazy
from theatre_core.utils.path import template_path


class DonorBackendListView(StaffuserRequiredMixin, ListView):
    ''' Start Page with listed Donors '''

    model = Donor
    template_name = template_path(Donor, 'backend', 'list')


class DonorCreateView(StaffuserRequiredMixin, CreateView):

    model = Donor
    form_class = DonorForm
    success_url = reverse_lazy('backend-donor-list')
    template_name = template_path(Donor, 'backend', 'create_form')


class DonorUpdateView(StaffuserRequiredMixin, UpdateView):

    model = Donor
    form_class = DonorForm
    success_url = reverse_lazy('backend-donor-list')
    template_name = template_path(Donor, 'backend', 'update_form')


class DonorDeleteView(StaffuserRequiredMixin, DeleteView):

    model = Donor
    success_url = reverse_lazy('backend-donor-list')
    template_name = template_path(Donor, 'backend', 'confirm_delete')
