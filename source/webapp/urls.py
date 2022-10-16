from django.urls import path

from webapp.views.base import ProductIndexView
from webapp.views.products import ProductView, ProductAddView, ProductUpdateView, TaskDeleteView


urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    path('products/', ProductIndexView.as_view(), name='index_view'),
    path('products/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('products/add/', ProductAddView.as_view(), name='product_add'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>', TaskDeleteView.as_view(), name='product_delete'),
]
