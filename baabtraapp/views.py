from django.shortcuts import render

# Create your views here.

def b_home(request):
    return render(request,'baabtraapp/home.html')

def about(request):
    return render(request,'baabtraapp/about.html')

def contact(request):
    return render(request,'baabtraapp/contact.html')

def boot_strap(request):
    return render(request,'baabtraapp/bootstrap.html')