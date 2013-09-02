# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.text import slugify
from easymode.i18n.decorators import I18n
from theatre_core.models import TimeStampedModel

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

