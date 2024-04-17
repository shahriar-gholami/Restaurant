from django import forms
from django.forms import formset_factory
from .models import Item


class ItemForm(forms.Form):
    item = forms.CharField()
    count = forms.IntegerField()

ItemsFormSet = formset_factory(ItemForm)


