from django.urls import path

from . import views

urlpatterns = [
    path('Signin', views.signNewUser, name="signNewUser"),
    path('Login', views.loginuser, name="loginuser"),
    path('Welcome', views.Welcomepage, name="Welcomepage"),
    path('Logout', views.logoutpage, name="logoutpage"),
    path('QuizzList', views.Quizzlistpage, name="Quizzlistpage"),
    path('QuizzCreation', views.Quizzcreationpage, name="Quizzcreationpage"),
    path('QuestionAjout', views.QuestionAjoutpage, name="QuestionAjoutpage")
]