from django import forms
from lakedata.models import WaterSample


class SiteSelectionForm(forms.ModelForm):
    year = forms.MultipleChoiceField(choices=[(x, x) for x in range(1987, 2006)])

    class Meta:
        model = WaterSample
        fields = ['site']


class MultiYearSelectionForm(forms.ModelForm):
    syear = forms.MultipleChoiceField(choices=[(x, x) for x in range(1987, 2006)])
    eyear = forms.MultipleChoiceField(choices=[(x, x) for x in range(1987, 2006)])

    class Meta:
        model = WaterSample
        fields = ['site']