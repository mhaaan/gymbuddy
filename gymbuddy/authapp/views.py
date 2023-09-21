from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        # Could also add some regex to check password for other conditions
        if password1 != password2:
            print('entered password check')
            messages.info(request, "Passwords do not match!")
            return redirect('/signup')
        
        try:
            if User.objects.get(username=email):
                messages.warning(request, "Email is already in use")
                return redirect('/signup')
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(username=email, password=password1, first_name=firstname, last_name=lastname)
        myuser.save()
        messages.success(request, "You account has been created!")
        return redirect('/login')

    return render(request, 'signup.html')

def handlelogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        myuser=authenticate(username=email, password=password1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/login')

    return render(request, 'handlelogin.html')

def handlelogout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect('/login')