# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from django import forms
from django.core.files.images import get_image_dimensions
from models import PerformanceDonor, PerformanceGenre, Performance


class PerformanceDonorForm(forms.ModelForm):
    class Meta:
        model = PerformanceDonor

    def clean_donor_logo(self):

        picture = self.cleaned_data['donor_logo']
        if not picture:
            raise forms.ValidationError(_(u'No picture'))
        else:
            w, h = get_image_dimensions(picture)
            if h > 110:
                raise forms.ValidationError(
                      (u'Image must have a maximum 110px')
                      )
            return picture
