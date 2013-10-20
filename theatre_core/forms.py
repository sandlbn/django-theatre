# -*- coding: utf-8 -*-
from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):
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

        model = Donor

