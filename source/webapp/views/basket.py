from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from webapp.models import Basket, Product
from webapp.forms import BasketForm


class BasketAddView(CreateView):
    model = Basket
    form_class = BasketForm
    template_name = 'partial/basket_form.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        quantity = form.cleaned_data.get("quantity")
        message = f"<h3>Rest of {product.title} in warehouse {product.rest}. Can't add {quantity} pc. in basket </h3>" \
                  f"<a href='/'><h3 class='masthead-brand'>Go back</h3></a>"
        try:
            basket = Basket.objects.get(product=product)
        except Basket.DoesNotExist:
            if product.rest == 0:
                return HttpResponseBadRequest(message)
            else:
                basket = Basket.objects.create(product=product)
        if quantity > product.rest:
            basket.delete()
            return HttpResponseBadRequest(message)
        else:
            if not basket:
                basket.quantity = quantity
            else:
                basket.quantity += quantity
            if basket.quantity > product.rest:
                return HttpResponseBadRequest(message)
            basket.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('index')


class BasketView(ListView):
    model = Basket
    template_name = "basket/basket_index.html"
    context_object_name = "basket"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['get_total'] = Basket.get_total()
        # context['form'] = OrderForm()
        return context


class BasketDeleteView(DeleteView):
    model = Basket
    success_url = reverse_lazy('basket_view')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
