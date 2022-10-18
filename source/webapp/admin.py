from django.contrib import admin

from webapp.models import Product, Basket


class ProductsListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'image', 'category', 'rest', 'price']
    list_filter = ['id', 'title', 'description', 'image', 'category', 'rest', 'price']
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
