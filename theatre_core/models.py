# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from django.db import models
from django.utils.translation import ugettext as _
from easymode.i18n.decorators import I18n
from django.contrib.sites.models import get_current_site


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
class MenuTop(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    link = models.CharField(max_length=255, verbose_name=_(u'Link'),
                            null=False, blank=False)
    position = models.IntegerField(verbose_name=_('Position'))
    parent = models.ForeignKey('self', verbose_name=u'Parent Model')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):

        request = None
        return ''.join(
            [
                'http://',
                get_current_site(request).domain,
                self.link
            ]
        )


@I18n('name')
class MenuBottom(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'),
                            null=False, blank=False, unique=True)
    link = models.CharField(max_length=255, verbose_name=_(u'Link'),
                            null=False, blank=False)
    position = models.IntegerField(verbose_name=_('Position'))
    parent = models.ForeignKey('self', verbose_name=u'Parent Model')

    def __unicode__(self):
        return self.name
