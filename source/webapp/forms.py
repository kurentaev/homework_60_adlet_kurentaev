from django import forms
from webapp.models import StatusChoices, Product, Order
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


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'address', 'phone')
