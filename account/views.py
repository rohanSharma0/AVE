from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth , User
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']

        user = auth.authenticate(username= email, password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pwd1 = request.POST['pwd1']
        pwd = request.POST['pwd']
        first_name,last_name = name.split(" ")

        if pwd1==pwd:

            if User.objects.filter(email = email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')

            else:
                user = User.objects.create_user(username=email,email=email,password=pwd,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('../login/')
        else:
            messages.info(request,'Password does not matching')
            return redirect('register')
    else:
        return render(request,'register.html')
