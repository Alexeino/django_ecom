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
    image = models.ImageField(upload_to="media/")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    stock = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.title