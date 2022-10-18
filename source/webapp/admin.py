from django.contrib import admin
from webapp.models import Product, Basket, Order


class ProductsListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'rest', 'price']
    list_filter = ['id', 'title', 'category', 'rest', 'price']
    search_fields = ['title', 'category']
    fields = ['id', 'title', 'description', 'image', 'category', 'rest', 'price']
    readonly_fields = ['id']


admin.site.register(Product, ProductsListAdmin)


class BasketListAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity']
    list_filter = ['product', 'quantity']
    search_fields = ['product', 'quantity']
    fields = ['product', 'quantity']


admin.site.register(Basket, BasketListAdmin)


class OrderListAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'address']
    list_filter = ['name', 'phone']
    search_fields = ['name', 'phone']
    fields = ['name', 'phone', 'address']


admin.site.register(Order, OrderListAdmin)
