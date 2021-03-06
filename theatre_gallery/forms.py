# -*- coding: utf-8 -*-
from django import forms
from .models import Gallery
from .models import Photo
from tinymce.widgets import TinyMCE


class GalleryForm(forms.ModelForm):
    name_ue = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span10'}
        )
    )
    name_pl = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span10'}
        )
    )
    name_en = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span10'}
        )
    )
    description_en = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span10',
                'cols': 80,
                'rows': 20
            }
        )
    )
    description_ue = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span6',
                'width': 20
            }
        )
    )
    description_pl = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span10',
                'cols': 80,
                'rows': 20
            }
        )
    )
    author = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span10'}
        )
    )

    class Meta:

        model = Gallery
        exclude = ('slug',)


class PhotoForm(forms.ModelForm):
    name_ue = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span10'}
        )
    )
    name_pl = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span10'}
        )
    )
    name_en = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'class': 'span10'}
        )
    )

    class Meta:

        model = Photo
        widgets = {
            'gallery': forms.widgets.HiddenInput()
        }
