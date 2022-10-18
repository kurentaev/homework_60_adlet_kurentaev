from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from webapp.models import Basket, Product, Order, ProductOrder
from webapp.forms import BasketForm, OrderForm


def get_success_url(self):
    return reverse('index')


class BasketAddView(CreateView):
    model = Basket
    form_class = BasketForm
    template_name = 'partial/basket_form.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        quantity = form.cleaned_data.get("quantity")
        try:
            basket = Basket.objects.get(product=product)
        except Basket.DoesNotExist:
            if product.rest == 0:
                return HttpResponseRedirect(get_success_url(self))
            else:
                basket = Basket.objects.create(product=product)
        if quantity > product.rest:
            basket.delete()
            return HttpResponseRedirect(get_success_url(self))
        else:
            if not basket:
                basket.quantity = quantity
            else:
                basket.quantity += quantity
            if basket.quantity > product.rest:
                return HttpResponseRedirect(get_success_url(self))
            basket.save()
        return HttpResponseRedirect(get_success_url(self))


class BasketView(ListView):
    model = Basket
    template_name = "basket/basket_index.html"
    context_object_name = "basket"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['get_total'] = Basket.get_total()
        context['form'] = OrderForm()
        return context


class BasketDeleteView(DeleteView):
    model = Basket
    success_url = reverse_lazy('basket_view')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class OrderAddView(CreateView):
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        order = form.save()
        products = []
        in_basket = []
        for item in Basket.objects.all():
            in_basket.append(ProductOrder(product=item.product, quantity=item.quantity, order=order))
            item.product.rest -= item.quantity
            products.append(item.product)
        ProductOrder.objects.bulk_create(in_basket)
        Product.objects.bulk_update(products, ("rest",))
        Basket.objects.all().delete()
        return HttpResponseRedirect(get_success_url(self))
