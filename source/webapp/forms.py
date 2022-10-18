from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from webapp.models import StatusChoices, Product

from webapp.models import Basket


class ProductsListForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'rest', 'price')


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=200,
        required=False,
        label='Search'
    )


class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ('quantity',)
