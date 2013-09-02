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
    template_name = 'admin/news_create_form.html'


class NewsUpdateView(UpdateView):

    model = News
    template_name = 'admin/news_update_form.html'


class NewsDeleteView(DeleteView):

    model = News
    success_url = reverse_lazy('admin-news-list')
    template_name = 'admin/news_confirm_delete_form.html'


class NewsListView(ListView):

    model = News
    template_name = 'admin/news_list.html'


class NewsDetailView(DetailView):

    model = News
    template_name = 'frontend/news_detail.html'


class StaticPageCreateView(CreateView):

    model = StaticPage
    template_name = 'admin/static_page_create_form.html'


class StaticPageUpdateView(UpdateView):

    model = StaticPage
    template_name = 'admin/static_page_update_form.html'


class StaticPageDeleteView(DeleteView):

    model = StaticPage
    success_url = reverse_lazy('admin-news-list')
    template_name = 'admin/static_page_confirm_delete.html'


class StaticPageListView(ListView):

    model = StaticPage
    template_name = 'admin/static_page_list.html'


class StaticPageDetailView(DetailView):

    model = StaticPage
    template_name = 'frontend/static_page_detail.html'

