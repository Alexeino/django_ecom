from rest_framework import serializers
from products.models import Product, ItemImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    product_images = ImageSerializer(many=True,read_only=True)
    class Meta:
        model = Product
        fields = ['id','title','description','price','category','stock','product_images']
        required_fields = ('title','description',
                           'price','category','products')