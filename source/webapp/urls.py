from django.urls import path
from webapp.views.base import ProductIndexView
from webapp.views.products import ProductView, ProductAddView, ProductUpdateView, TaskDeleteView
from webapp.views.basket import BasketAddView, BasketView, BasketDeleteView

urlpatterns = [
    path('', ProductIndexView.as_view(), name='index'),
    path('products/', ProductIndexView.as_view(), name='index_view'),
    path('products/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('products/add/', ProductAddView.as_view(), name='product_add'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>', TaskDeleteView.as_view(), name='product_delete'),
    path('products/basket/add/<int:pk>', BasketAddView.as_view(), name='product_basket_add'),
    path('products/basket/', BasketView.as_view(), name='basket_view'),
    path('products/basket/delete/<int:pk>', BasketDeleteView.as_view(), name='product_basket_delete'),
]
