from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id','title','price','image','category','stock')
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)