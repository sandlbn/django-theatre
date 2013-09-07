# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from django import forms
from tinymce.widgets import TinyMCE
from django.core.files.images import get_image_dimensions
from django.utils.translation import ugettext as _
from .models import PerformanceDonor
from .models import PerformanceGenre
from .models import Performance
from .models import PerformanceTime


class PerformanceDonorForm(forms.ModelForm):
    """
    Model form for PerformanceDonor
    """
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
                    _(u'Image can not be higher than 110px')
                )
            return picture


class PerformanceGenreForm(forms.ModelForm):
    """
    Modelform for PerformanceGenre
    """
    name_ue = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span8'}
        )
    )
    name_pl = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span8'}
        )
    )
    name_en = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span8'}
        )
    )

    class Meta:
        model = PerformanceGenre
        exclude = ('slug',)


class PerformanceForm(forms.ModelForm):
    """
    Modelform for Performance
    """
    name_ue = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span8'}
        )
    )
    name_pl = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span8'}
        )
    )
    name_en = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span8'}
        )
    )
    description_en = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span8',
                'cols': 80,
                'rows': 20
            }
        )
    )
    description_ue = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span8',
                'cols': 80,
                'rows': 20
            }
        )
    )
    description_pl = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span8',
                'cols': 80,
                'rows': 20
            }
        )
    )

    class Meta:

        exclude = ('slug',)
        model = Performance


class PerformanceTimeForm(forms.ModelForm):
    """
    Modelform for Performance Time
    """
    class Meta:

        exclude = ('slug',)
        model = PerformanceTime
