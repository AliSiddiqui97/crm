from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("Must have email")
        if not name:
            raise ValueError("Must have email")
        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True

        user.save(using=self._db)
        return user
        

class Customer(AbstractBaseUser):
    name = models.CharField(max_length=50,null=True,unique=True )
    phone = models.CharField(max_length=50,null=True)
    email = models.EmailField(verbose_name="email",max_length=20,unique=True)
    profile_pic = models.ImageField(null=True,default='index.png')
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True )
    last_login = models.DateTimeField(verbose_name="last login",auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()
    def __str__(self):
        return self.name
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True



class Tag(models.Model):
    name = models.CharField(max_length=50,null=True )
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY =(
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),

    )
    name = models.CharField(max_length=20,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=20,null=True,choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)
    desciption = models.CharField(max_length=100,null=True,blank=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(null=True,default='product.png')

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery', 'Out for delivery' ),
        ('Delivered','Delivered'),
    )
    
    customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)
    status = models.CharField(max_length=40,null=True,choices=STATUS)
    def __str__(self):
        return self.product.name
    