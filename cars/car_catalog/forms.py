from django import forms

from car_catalog.models import Mark


class MarkForm(forms.ModelForm):

    class Meta:
        model = Mark
        fields = ['name']
