from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

'''
Performance description 
'''
class Performance(models.Model):
    name = models.CharField(max_length=255, verbose_name=_(u'Name'), null=False, blank=False)
    description = models.TextField(verbose_name=_(u'Description'))
    created = models.DateTimeField(verbose_name=_('Date published'),default=timezone.now)
    edited = models.DateTimeField(verbose_name=_('Date edited'))
    def __unicode__(self):
        return self.name
    
'''
Performance Schedule 
'''  
class PerformanceTime(models.Model):
    performance = models.ForeignKey(Performance, verbose_name=_(u'Performance'))
    performance_date = models.DateTimeField(verbose_name=_(u'Time'))
    published = models.BooleanField(verbose_name=_(u'Is Published ?'))
    
    def __unicode__(self):
        return u'{0} {1}'.format(self.performance.name, self.performance_date)