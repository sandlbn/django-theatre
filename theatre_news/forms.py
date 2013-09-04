from django import forms
from .models import StaticPage
from .models import News
from tinymce.widgets import TinyMCE


class StaticPageForm(forms.ModelForm):
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
    long_text_en = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span8',
                'cols': 80,
                'rows': 20
            }
        )
    )
    long_text_ue = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span8',
                'cols': 80,
                'rows': 20
            }
        )
    )
    long_text_pl = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span8',
                'cols': 80,
                'rows': 20
            }
        )
    )

    class Meta:

        model = StaticPage
        exclude = ('slug',)


class NewsForm(forms.ModelForm):

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
    short_text_ue = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={'class': 'span8'}
        )
    )
    short_text_pl = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={'class': 'span8'}
        )
    )
    short_text_en = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={'class': 'span8'}
        )
    )
    long_text_en = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span8',
                'cols': 80,
                'rows': 20
            }
        )
    )
    long_text_ue = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span8',
                'cols': 80,
                'rows': 20
            }
        )
    )
    long_text_pl = forms.CharField(
        widget=TinyMCE(
            attrs={
                'class': 'span8',
                'cols': 80,
                'rows': 20
            }
        )
    )

    class Meta:
        model = News
        exclude = ('slug',)
