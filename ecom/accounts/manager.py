from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self,mobile,password=None,**extra_fields):
        if not mobile:
            raise ValueError("Phone number is required...")
        if not password:
            raise ValueError("Password is required..")
        
        user = self.model(mobile=mobile,**extra_fields)
        user.set_password(password)
        
        user.save()
        
        return user
    
    # Not required for now
    def create_superuser(self,mobile, password,**extra_fields):
        if not mobile:
            raise ValueError("Phone number is required...")
        if not password:
            raise ValueError("Password is required..")
        
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        return self.create_user(mobile,password,**extra_fields)