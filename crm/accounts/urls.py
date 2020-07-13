from django.urls import path
from . import views

urlpatterns = [   
     path('',views.home,name='home'),
     
     path('signin/',views.signinPage, name='signinPage'),
     path('signup/',views.signupPage, name='signupPage'),
     path('login/',views.loginPage,name='loginPage'),
     path('products/' , views.productPage, name='productPage'),
     path('customers/' , views.customerPage, name='customerPage'),
     path('settings/' , views.settingPage, name='settingPage'),
     
     
]