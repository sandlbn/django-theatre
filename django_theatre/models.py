# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from easymode.i18n.decorators import I18n
from django.template.defaultfilters import slugify
from PIL import Image


@I18n('name')
class PerformanceGenre(models.Model):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                             null=False, blank=False, unique=True)
    slug = models.SlugField(verbose_name=_(u'Slug'))
    created = models.DateTimeField(verbose_name=_('Date created'),
                                   default=timezone.now)
    edited = models.DateTimeField(verbose_name=_('Date edited'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

    def __unicode__(self):
        return self.name


@I18n('description')
@I18n('name')
class Performance(models.Model):
    '''Performance description '''
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                             null=False, blank=False, unique=True)
    description = models.TextField(verbose_name=_(u'Description'))
    payroll = models.TextField(verbose_name=_(u'Payroll'))
    genre = models.ForeignKey(PerformanceGenre)
    slug = models.SlugField(verbose_name=_(u'Slug'))
    created = models.DateTimeField(verbose_name=_('Date published'),
                                   default=timezone.now)
    edited = models.DateTimeField(verbose_name=_('Date edited'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

    def __unicode__(self):
        return self.name


class PerformanceTime(models.Model):
    '''Performance Schedule '''
    performance = models.ForeignKey(Performance,
                                    verbose_name=_(u'Performance'))
    performance_date = models.DateTimeField(verbose_name=_(u'Time'))
    event_of_month = models.BooleanField(verbose_name=_(u'Event of month ?'))
    published = models.BooleanField(verbose_name=_(u'Is Published ?'))

    def __unicode__(self):
        return u'{0} {1}'.format(self.performance.name, self.performance_date)


@I18n('name')
class PerformanceDonor(models.Model):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                             null=False, blank=False, unique=True)
    donor_logo = models.ImageField(upload_to='donors/logo',
                                   verbose_name=_(u'Donor Logo'),
                                   blank=True, null=True)
    link = models.URLField(verbose_name=u'Link', blank=True, null=True)
    performance = models.ForeignKey(Performance)
    created = models.DateTimeField(verbose_name=_('Date created'),
                                   default=timezone.now)
    edited = models.DateTimeField(verbose_name=_('Date edited'))

    def __unicode__(self):
        return self.name


@I18n('long_text')
@I18n('short_text')
@I18n('name')
class News(models.Model):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                             null=False, blank=False, unique=True)
    short_text = models.CharField(max_length=255,
                                  verbose_name=_(u'Short Text'))
    long_text = models.TextField(verbose_name=_(u'Long Text'))
    slug = models.SlugField(verbose_name=_(u'Slug'))
    published = models.BooleanField(verbose_name=_(u'Is Published ?'))
    created = models.DateTimeField(verbose_name=_('Date published'),
                                   default=timezone.now)
    edited = models.DateTimeField(verbose_name=_('Date edited'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

    def __unicode__(self):
        return self.name


@I18n('long_text')
@I18n('name')
class StaticPage(models.Model):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                             null=False, blank=False, unique=True)
    long_text = models.TextField(verbose_name=_(u'Long Text'))
    slug = models.SlugField(verbose_name=_(u'Slug'))
    published = models.BooleanField(verbose_name=_(u'Is Published ?'))
    created = models.DateTimeField(verbose_name=_('Date published'),
                                   default=timezone.now)
    edited = models.DateTimeField(verbose_name=_('Date edited'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

    def __unicode__(self):
        return self.name
