from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('Signin', views.signNewUser, name="signNewUser"),
    path('Login', views.loginuser, name="loginuser"),
    path('Welcome', views.Welcomepage, name="Welcomepage"),
    path('Logout', views.logoutpage, name="logoutpage")
]