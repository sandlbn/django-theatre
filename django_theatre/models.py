# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from easymode.i18n.decorators import I18n
from django.template.defaultfilters import slugify


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating
    ``created`` and ``modified`` fields. following @pydanny
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@I18n('name')
class PerformanceGenre(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    slug = models.SlugField(verbose_name=_(u'Slug'))

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)

    def __unicode__(self):
        return self.name


@I18n('description', 'name')
class Performance(TimeStampedModel):
    '''Performance description '''
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    description = models.TextField(verbose_name=_(u'Description'))
    payroll = models.TextField(verbose_name=_(u'Payroll'))
    photo = models.ImageField(upload_to='performance/photo',
                              verbose_name=_(u'Photo')
                              )
    genre = models.ForeignKey(PerformanceGenre)
    slug = models.SlugField(verbose_name=_(u'Slug'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

    def __unicode__(self):
        return self.name


class PerformanceTime(TimeStampedModel):
    '''Performance Schedule '''
    performance = models.ForeignKey(Performance,
                                    verbose_name=_(u'Performance'))
    performance_date = models.DateTimeField(verbose_name=_(u'Time'))
    event_of_month = models.BooleanField(verbose_name=_(u'Event of month ?'))
    slug = models.SlugField(verbose_name=_(u'Slug'))
    published = models.BooleanField(verbose_name=_(u'Is Published ?'))
    frontpage = models.BooleanField(verbose_name=_(u'On FrontPage ?'))

    def save(self, *args, **kwargs):
        ''' create a slug string performance,2012,23,12,19,00 '''
        if not self.id:
            self.slug = slugify(
                "{0},{1},{2},{3},{4},{5}".format(
                    self.performance.name,
                    self.performance_date.year,
                    self.performance_date.month,
                    self.performance_date.day,
                    self.performance_date.hour,
                    self.performance_date.min,
                )
            )

    def __unicode__(self):
        return u'{0} {1}'.format(self.performance.name, self.performance_date)


@I18n('name')
class PerformanceDonor(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    donor_logo = models.ImageField(upload_to='donors/logo',
                                   verbose_name=_(u'Donor Logo'),
                                   blank=True, null=True)
    link = models.URLField(verbose_name=u'Link', blank=True, null=True)
    performance = models.ForeignKey(Performance)

    def __unicode__(self):
        return self.name


@I18n('long_text', 'short_text', 'name')
class News(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    short_text = models.CharField(max_length=255,
                                  verbose_name=_(u'Short Text'))
    long_text = models.TextField(verbose_name=_(u'Long Text'))
    slug = models.SlugField(verbose_name=_(u'Slug'))
    published = models.BooleanField(verbose_name=_(u'Is Published ?'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

    def __unicode__(self):
        return self.name


@I18n('long_text', 'name')
class StaticPage(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    long_text = models.TextField(verbose_name=_(u'Long Text'))
    slug = models.SlugField(verbose_name=_(u'Slug'))
    published = models.BooleanField(verbose_name=_(u'Is Published ?'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

    def __unicode__(self):
        return self.name


@I18n('name')
class MenuTop(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    link = models.CharField(max_length=255, verbose_name=_(u'Link'),
                            null=False, blank=False)
    position = models.IntegerField(verbose_name=_('Position'))

    def __unicode__(self):
        return self.name


@I18n('name')
class MenuBottom(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    link = models.CharField(max_length=255, verbose_name=_(u'Link'),
                            null=False, blank=False)
    position = models.IntegerField(verbose_name=_('Position'))

    def __unicode__(self):
        return self.name
