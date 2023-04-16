from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    stock = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    
class ItemImage(models.Model):
    meta_data = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media/")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_images")
    
    def __str__(self):
        return self.image.url