# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from django.db import models
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _
from theatre_core.models import TimeStampedModel
from django_bootstrap_calendar.models import CalendarEvent
from easymode.i18n.decorators import I18n
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
import datetime


@I18n('name')
class PerformanceGenre(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    css_class = models.CharField(max_length=255,
                                 verbose_name=_(u'CSS class name'),
                                 null=False, blank=False, unique=True)
    slug = models.SlugField(verbose_name=_(u'Slug'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(PerformanceGenre, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


@I18n('name', 'description')
class Performance(TimeStampedModel):
    '''Performance description '''
    photo = models.ImageField(upload_to='performance/photo',
                              verbose_name=_(u'Photo')
                              )
    genre = models.ForeignKey(PerformanceGenre)
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    description = models.TextField(verbose_name=_(u'Description'))
    payroll = models.TextField(verbose_name=_(u'Payroll'))
    slug = models.SlugField(verbose_name=_(u'Slug'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Performance, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class PerformanceTime(TimeStampedModel):
    '''Performance Schedule '''
    performance = models.ForeignKey(Performance,
                                    verbose_name=_(u'Performance'))
    performance_date = models.DateField(verbose_name=_(u'Date'))
    performance_time = models.TimeField(verbose_name=_(u'Time'))
    published = models.BooleanField(verbose_name=_(u'Is Published ?'))
    event_of_month = models.BooleanField(verbose_name=_(u'Event of month ?'))
    program_id = models.IntegerField(max_length='5',
                                     verbose_name=_('System number'))
    slug = models.SlugField(verbose_name=_(u'Slug'))

    def save(self, *args, **kwargs):
        ''' create a slug string eg: performance__2012_23_12__19_00 '''
        if not self.id:
            self.slug = "{0}__{1}__{2}".format(
                slugify(self.performance.name),
                self.performance_date.strftime("%d_%m_%Y"),
                self.performance_time.strftime("%H_%M")
            )
        super(PerformanceTime, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'{0} {1}'.format(self.performance.name, self.performance_date)

    @property
    def performance_date_str(self):
        return self.performance_date.strftime("%d-%m-%Y")

    @property
    def performance_time_str(self):
        return self.performance_date.strftime("%H:%M")

    def get_absolute_url(self):
        return reverse_lazy(
            'frontend-performance-time-detail',
            args=[self.slug]
        )


def django_calendar(sender, instance, **kwargs):
    events = CalendarEvent.objects.filter(url=instance.get_absolute_url())
    if events.count() > 0:
        for event in events:
            event.delete()
    new_event = CalendarEvent()
    new_event.title = instance.performance.name_pl
    new_event.start = datetime.datetime(
        instance.performance_date.year,
        instance.performance_date.month,
        instance.performance_date.day,
        instance.performance_time.hour,
        instance.performance_time.minute,
        instance.performance_time.second
    )
    new_event.end = datetime.datetime(
        instance.performance_date.year,
        instance.performance_date.month,
        instance.performance_date.day,
        instance.performance_time.hour,
        instance.performance_time.minute,
        instance.performance_time.second
    )
    new_event.url = instance.get_absoulute_url()
    new_event.css_class = instance.performance.genre.css_class
    new_event.save()

post_save.connect(django_calendar, sender=PerformanceTime)

@I18n('name')
class PerformanceDonor(TimeStampedModel):
    DONOR_TYPE_CHOICES = (
        ('sp', _('Sponsor')),
        ('pr', _(u'Press'))
    )
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    donor_logo = models.ImageField(upload_to='donors/logo',
                                   verbose_name=_(u'Donor Logo'),
                                   blank=True, null=True)
    donor_type = models.CharField(max_length=2,
                                  verbose_name=_(u'Donor Type'),
                                  choices=DONOR_TYPE_CHOICES,
                                  default='sponsor')
    link = models.URLField(verbose_name=u'Link', blank=True, null=True)
    performance = models.ForeignKey(Performance)

    def __unicode__(self):
        return self.name


class PerformanceFrontPage(TimeStampedModel):
    span_width = models.IntegerField(
        max_length=2, verbose_name=_(u'Span Width'), null=False, blank=False)
    preformance_time = models.ForeignKey(PerformanceTime,
                                         null=True, blank=True)
    short_description = models.TextField(verbose_name=_('Short Description'))
    photo = models.ImageField(upload_to='frontend/photo',
                              verbose_name=_(u'Photo')
                              )

    def __unicode__(self):
        return self.performance_time.performance.name
