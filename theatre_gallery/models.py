# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from easymode.i18n.decorators import I18n
from theatre_core.models import TimeStampedModel
from theatre_performance.models import Performance


@I18n('name', 'description')
class Gallery(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'),
                            null=False, blank=False, unique=True)
    description = models.TextField(verbose_name=_('Description'),
                                   blank=True)
    author = models.CharField(max_length=255, verbose_name=_('Author Name'),
                              blank=True, null=True)
    slug = models.SlugField(verbose_name=_('Slug'))
    performance = models.ForeignKey(Performance, blank=True, null=True)
    published = models.BooleanField(verbose_name=_(u'Is Published ?'))

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Gallery, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('frontend-gallery-detail', args=[self.slug])


@I18n('name')
class Photo(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'),
                            blank=True, null=True)
    description = models.TextField(verbose_name=_('Description'),
                                   blank=True)
    picture = models.ImageField(verbose_name=_('Photo'), upload_to='gallery')
    gallery = models.ForeignKey(Gallery, verbose_name=_('Gallery'))

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('frontend-picture-detail', args=[self.pk])
