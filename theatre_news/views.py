# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from .models import News
from .models import StaticPage
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.core.urlresolvers import reverse_lazy


class NewsCreateView(CreateView):

    model = News
    template_name_suffix = '_create_form'


class NewsUpdateView(UpdateView):

    model = News
    template_name_suffix = '_update_form'


class NewsDeleteView(DeleteView):

    model = News
    success_url = reverse_lazy('admin-news-list')

class NewsListView(ListView):

    model = News

class NewsDetailView(DetailView):

    model = News


class StaticPageCreateView(CreateView):

    model = StaticPage
    template_name_suffix = '_create_form'


class StaticPageUpdateView(UpdateView):

    model = StaticPage
    template_name_suffix = '_update_form'


class StaticPageDeleteView(DeleteView):

    model = StaticPage
    success_url = reverse_lazy('admin-news-list')


class StaticPageListView(ListView):

    model = StaticPage


class StaticPageDetailView(DetailView):

    model = StaticPage

