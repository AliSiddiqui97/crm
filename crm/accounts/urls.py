from django.urls import path
from . import views

urlpatterns = [   
     path('',views.home,name='home'),
     path('customer/<str:pk>/',views.home2,name='home_customer'),
     
     path('signin/',views.signinPage, name='signinPage'),
     path('signup/',views.signupPage, name='signupPage'),
     path('logout/',views.logoutPage, name='logoutPage'),
     
     path('products/' , views.productPage, name='productPage'),
     path('customers/' , views.customerPage, name='customerPage'),
     path('settings/' , views.settingPage, name='settingPage'),
     
     
]