from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from .forms import *
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

def Categorielistpage(request):
    categorielist = Categorie.objects.all()
    return render(request, 'categoriesList.html', {'categorielist': categorielist})

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


def QuestionAjoutpage(request):
    if request.method == "POST":
        form = QuestionAjoutForm(request.POST)
        if form.is_valid():
            try:
                savequestion = Question(question_text = request.POST.get('question_text'), reponse_text = request.POST.get('reponse_text'), quizz = Quizz.objects.get(id=request.POST.get('quizz')))
                savequestion.save()
                return render(request, 'QuestionAjout.html', {'form':form, 'info':'La question a été créé..!'})
            except IntegrityError:
                return render(request, 'QuestionAjout.html', {'form':form, 'error':'La question existe deja..!'})
        else:
            return render(request, 'QuestionAjout.html', {'form':form, 'error':'ERREUR la question n\'as pas été créé..!'})
    else:
        form = QuestionAjoutForm()
    return render(request, 'QuestionAjout.html', {'form':form})


def QuizzDetails(request, quizz_id):
    quizz = get_object_or_404(Quizz, pk=quizz_id)
    questionList = Question.objects.filter(quizz = quizz_id)
    score = None
    if request.method == "POST":
        for question in questionList:
            if score is None:
                score = 0
            if request.POST.get('reponse'+str(question.id)).lower() == question.reponse_text.lower():
                score += 1
    return render(request, 'QuizzDetails.html', {'quizz': quizz, 'questionList': questionList, 'score': score})