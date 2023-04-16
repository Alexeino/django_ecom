from django.contrib import admin
from .models import Product, Category,ItemImage

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('id','title','price','category','stock')
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(ItemImage)