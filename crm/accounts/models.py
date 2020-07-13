from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50,null=True )
    phone = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=20,null=True)
    date_created = models.DateTimeField(auto_now_add=True ,null=True)
    profile_pic = models.ImageField(null=True,default='index.png')
    admin = models.CharField(max_length=2,null=True,default='0')
    
    def __str__(self):
        return self.name


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
    