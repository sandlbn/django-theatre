# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from django.conf import settings

if not settings.LANGUAGES:
    LANGUAGES = (('en', 'English'), ('pl', 'Polish'), ('ue', 'Ukraine'),)
