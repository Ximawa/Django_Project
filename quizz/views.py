from django.db import IntegrityError
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import SignInForm, AuthenticateForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def signNewUser(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            try:
                saveuser = User.objects.create_user(request.POST.get('username'), password=request.POST.get('password'))
                saveuser.save()
                return render(request, 'Signup.html', {'form':form, 'info':'L\'utilisateur '+request.POST.get('username')+' a été créé..!'})
            except IntegrityError:
                return render(request, 'Signup.html', {'form':form, 'error':'L\'utilisateur '+request.POST.get('username')+' existe deja..!'})
        else:
            return render(request, 'Signup.html', {'form':form, 'error':'L\'utilisateur '+request.POST.get('username')+' n\'a pas été créé..!'})  
    else:
        form = SignInForm()
    return render(request, 'Signup.html', {'form':form})

def loginuser(request):
    if request.method == "POST":
        loginsuccess = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if loginsuccess is None:
            return render(request, 'Login.html',{'form': AuthenticateForm(), 'error':'Username ou Password ne correspondent pas à la base de données..!'})
        else:
            login(request, loginsuccess)
            return redirect('Welcomepage')
    else:
        return render(request, 'Login.html',{'form': AuthenticateForm()})

def Welcomepage(request):
    return render(request,'Welcome.html')

def logoutpage(request):
    if request.method == "POST":
        logout(request)
        return redirect('Welcomepage')