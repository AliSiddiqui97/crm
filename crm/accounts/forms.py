from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['name','phone','email']
        exclude = ['admin','profile_pic','is_admin','is_active','is_superuser','is_staff']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        