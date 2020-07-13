from django.shortcuts import render

def signinPage(request):
    context = {}
    return render(request, 'accounts/signin.html',context )

def signupPage(request):
    context = {}
    return render(request, 'accounts/signup.html',context )

def home(request):
    context = {}
    return render(request, 'accounts/dashboard.html',context )


def loginPage(request):

    context = {}
    return render(request,'accounts/login.html',context )


def productPage(request):
    context = {}
    return render(request,'accounts/products.html',context)


def customerPage(request):
    context = {}
    return render(request,'accounts/customer.html',context)

def settingPage(request):
    context = {}
    return render(request,'accounts/settings.html',context)

