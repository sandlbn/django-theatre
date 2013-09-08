# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from .models import Gallery
from .models import Photo
from .forms import GalleryForm
from .forms import PhotoForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from braces.views import StaffuserRequiredMixin
from django.core.urlresolvers import reverse_lazy
from theatre_core.utils.path import template_path


class GalleryBackendListView(ListView):

    model = Gallery
    template_name = template_path(model, 'backend', 'list')


class GalleryCreateView(CreateView, StaffuserRequiredMixin):

    model = Gallery
    form_class = GalleryForm
    success_url = reverse_lazy('backend-gallery-list')
    template_name = template_path(model, 'backend', 'create_form')


class GalleryUpdateView(UpdateView, StaffuserRequiredMixin):

    model = Gallery
    form_class = GalleryForm
    success_url = reverse_lazy('backend-gallery-list')
    template_name = template_path(model, 'backend', 'update_form')


class GalleryDeleteView(DeleteView, StaffuserRequiredMixin):

    model = Gallery
    success_url = reverse_lazy('backend-gallery-list')
    template_name = template_path(model, 'backend', 'confirm_delete')


class PhotoBackendListView(ListView):

    model = Photo
    template_name = template_path(model, 'backend', 'list')

    def get_queryset(self):
        return self.model.objects.filter(gallery_id=self.kwargs['gallery'])


class PhotoCreateView(CreateView, StaffuserRequiredMixin):

    model = Photo
    form_class = PhotoForm
    success_url = reverse_lazy('backend-photo-list')
    template_name = template_path(model, 'backend', 'create_form')


class PhotoUpdateView(UpdateView, StaffuserRequiredMixin):

    model = Gallery
    form_class = GalleryForm
    success_url = reverse_lazy('backend-photo-list')
    template_name = template_path(model, 'backend', 'update_form')


class PhotoDeleteView(DeleteView, StaffuserRequiredMixin):

    model = Gallery
    success_url = reverse_lazy('backend-photo-list')
    template_name = template_path(model, 'backend', 'confirm_delete')
