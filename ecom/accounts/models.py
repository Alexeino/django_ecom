from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STAFF = "ST","STAFF"
        CUSTOMER = "CUST","CUSTOMER"
    
    mobile = models.CharField(max_length=15)
    role = models.CharField(max_length=8,choices=Role.choices)
    
    objects = UserManager()
    REQUIRED_FIELDS = ['mobile','role']