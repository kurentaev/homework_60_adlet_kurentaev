from django import forms
from webapp.models import StatusChoices, Product


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
