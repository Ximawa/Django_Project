from django.db import IntegrityError
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import QuizzCreationForm, SignInForm, AuthenticateForm, QuizzCreationForm
from .models import *


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

def Quizzlistpage(request):
    quizzlist = Quizz.objects.all()
    return render(request, 'QuizzList.html', {'quizzlist': quizzlist})

def Quizzcreationpage(request):
    if request.method == "POST":
        form = QuizzCreationForm(request.POST)
        if form.is_valid():
            try:
                savequizz = Quizz(nom = request.POST.get('nom'), categorie = Categorie.objects.get(id=request.POST.get('categorie')), createur= request.user)
                savequizz.save()
                return render(request, 'QuizzCreation.html', {'form':form, 'info':'Le quizz a été créé..!'})
            except IntegrityError:
                return render(request, 'QuizzCreation.html', {'form':form, 'error':'Le quizz existe deja..!'})
        else:
            return render(request, 'QuizzCreation.html', {'form':form, 'error':'ERREUR le quizz n\'as pas été créé..!'})
    else:
        form = QuizzCreationForm()
    return render(request, 'QuizzCreation.html', {'form':form})