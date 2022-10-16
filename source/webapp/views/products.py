from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
from webapp.forms import ProductsListForm


class ProductView(DetailView):
    template_name = 'product/product.html'
    model = Product
    context_object_name = 'product'


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductAddView(SuccessDetailUrlMixin, CreateView):
    template_name = 'product/product_add.html'
    form_class = ProductsListForm
    model = Product


class ProductUpdateView(SuccessDetailUrlMixin, UpdateView):
    template_name = 'product/product_update.html'
    form_class = ProductsListForm
    model = Product
    context_object_name = 'product'


class TaskDeleteView(DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('index')
