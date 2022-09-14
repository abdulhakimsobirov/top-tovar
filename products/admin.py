from django.contrib import admin
from .models import Category, Product, Request
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'count')
    list_filter = ('id', 'name', 'image', 'count')
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'price', 'image', 'video', 'top')
    list_filter = ('id', 'name', 'description', 'category', 'price', 'image', 'video', 'top')
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'phone', 'region')
    list_filter = ('id', 'client_name', 'phone', 'region')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Request, RequestAdmin)