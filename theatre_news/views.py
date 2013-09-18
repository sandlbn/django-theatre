# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from .models import News
from .models import StaticPage
from .forms import StaticPageForm
from .forms import NewsForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from braces.views import StaffuserRequiredMixin
from django.core.urlresolvers import reverse_lazy


class NewsCreateView(CreateView, StaffuserRequiredMixin):

    model = News
    form_class = NewsForm
    success_url = reverse_lazy('backend-news-list')
    template_name = 'theatre_news/backend/news_create_form.html'


class NewsUpdateView(UpdateView, StaffuserRequiredMixin):

    model = News
    form_class = NewsForm
    success_url = reverse_lazy('backend-news-list')
    template_name = 'theatre_news/backend/news_update_form.html'


class NewsDeleteView(DeleteView, StaffuserRequiredMixin):

    model = News
    success_url = reverse_lazy('backend-news-list')
    template_name = 'theatre_news/backend/news_confirm_delete.html'


class NewsListView(ListView):

    model = News
    template_name = 'theatre_news/frontend/news_list.html'

    def get_queryset(self):

        return self.model.objects.filter(
            published=True
        ).order_by('-id')


class NewsListBackendView(ListView, StaffuserRequiredMixin):

    model = News
    template_name = 'theatre_news/backend/news_list.html'


class NewsDetailView(DetailView):

    model = News
    template_name = 'theatre_news/frontend/news_detail.html'


class StaticPageCreateView(CreateView):

    model = StaticPage
    form_class = StaticPageForm
    success_url = reverse_lazy('backend-static-list')
    template_name = 'theatre_news/backend/static_page_create_form.html'


class StaticPageUpdateView(UpdateView):

    model = StaticPage
    form_class = StaticPageForm
    success_url = reverse_lazy('backend-static-list')
    template_name = 'theatre_news/backend/static_page_update_form.html'


class StaticPageDeleteView(DeleteView):

    model = StaticPage
    success_url = reverse_lazy('backend-static-list')
    template_name = 'theatre_news/backend/static_page_confirm_delete.html'


class StaticPageListView(ListView):

    model = StaticPage
    template_name = 'theatre_news/backend/static_page_list.html'


class StaticPageDetailView(DetailView):

    model = StaticPage
    template_name = 'theatre_news/frontend/static_page_detail.html'

