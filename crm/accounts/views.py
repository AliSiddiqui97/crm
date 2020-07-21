from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login,logout
from .forms import *

def signinPage(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
       
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                return redirect('/')
            else:
                return redirect('/customer/'+str(request.user.id))

        else:
            messages.info(request,'Username or Password is incorrect')
            
    context = {}
    
    return render(request, 'accounts/signin.html',context )

def signupPage(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/signin')
    
    context = {"form":form}
    return render(request, 'accounts/signup.html',context )
def logoutPage(request):
    logout(request)
    return redirect('/signin')

def home(request):
    if not request.user.is_authenticated:
        return redirect('/signin')
    if not request.user.is_superuser:
        return redirect('/customer/' +str(request.user.id))
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status= 'Pending').count()
    orders = orders[:5]
    context ={'Customers':customers,'Orders':orders,'total_orders':total_orders,'delivered':delivered,'pending':pending,'admin':'1'  } 
    return render(request, 'accounts/dashboard.html',context )


def home2(request,pk):
    
    if not request.user.is_authenticated:
        return redirect('/signin')
    
    
    customers = Customer.objects.get(id=request.user.id)
    # orders = customers.objects.all(id=pk)
    orders =  customers.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status= 'Pending').count()
    orders = orders[:5]
    context ={'Customers':customers,'Orders':orders,'total_orders':total_orders,'delivered':delivered,'pending':pending,'admin':'0'  } 
    if request.user.is_superuser:
        customers = Customer.objects.get(id=pk)
        # orders = customers.objects.all(id=pk)
        orders =  customers.order_set.all()
        total_orders = orders.count()
        delivered = orders.filter(status = 'Delivered').count()
        pending = orders.filter(status= 'Pending').count()
        orders = orders[:5]
        context ={'Orders':orders,'total_orders':total_orders,'delivered':delivered,'pending':pending,'admin':'0'  } 
        return render(request, 'accounts/dashboard.html',context )
    return render(request, 'accounts/dashboard.html',context )



def productPage(request):
    
    if not request.user.is_authenticated:
        return redirect('/signin')
    
    products = Product.objects.all()
    context = {'Products': products}
    return render(request,'accounts/products.html',context)


def customerPage(request):
    
    if not request.user.is_authenticated:
        return redirect('/signin')
    print(request.user)
    customer = Customer.objects.get(name=request.user)
    orders = customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status= 'Pending').count()
    print(customer.profile_pic.url)
    context = {"Customer":customer,"total_orders":total_orders,"delivered":delivered,"pending":pending}
    return render(request,'accounts/customer.html',context)

def settingPage(request):
    
    if not request.user.is_authenticated:
        return redirect('/signin')
    context = {}
    return render(request,'accounts/settings.html',context)

