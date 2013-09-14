from django.db import models
from theatre_core.models import Timestampable

class Chair(models.Model):

    sys_number = models.IntegerField(
        max_length=2,
        verbose_name=_(u'Chair system number')
    )
    chair_number = models.IntegerField(max_lenght=3, verbose_name=u'Number')
    chair_row = models.IntegerField(max_lenght=3, verbose_name=u'Row Number')

    def __unicode__(self):
        return self.chair_number


class Reservation(TimeStampable):
    user = models.ForeignKey(User)

    def __unicode__(self):
        return user
