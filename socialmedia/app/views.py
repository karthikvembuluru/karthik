from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'Register.html')

def login(request):
    return render(request,'login.html')

def edit_profile(request):
    return render(request,'edit_profile.html')

def view_profile(request):
    return render(request,'view_profile.html')

def change_password(request):
    return render(request,'change_password.html')

def logout(request):
    return render(request,'logout.html')
def base(request):
    return render(request,'base.html')

