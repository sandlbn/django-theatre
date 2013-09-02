# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from .models import News
from .models import StaticPage
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


class NewsCreateView(CreateView):

    model = News


class NewsUpdateView(UpdateView):

    model = News

class NewsDeleteView(DeleteView):

    model = News

class NewsListView(ListView):

    model = News

class NewsDetailView(DetailView):

    model = News


class StaticPageCreateView(CreateView):

    model = StaticPage

class StaticPageUpdateView(UpdateView):

    model = StaticPage

class StaticPageDeleteView(DeleteView):

    model = StaticPage

class StaticPageListView(ListView):

    model = StaticPage

class StaticPageDetailView(DetailView):

    model = StaticPage

