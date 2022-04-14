from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views



urlpatterns = [
    path('Signin', views.signNewUser, name="signNewUser"),
    path('Login', views.loginuser, name="loginuser"),
    path('Welcome', views.Welcomepage, name="Welcomepage"),
    path('Logout', views.logoutpage, name="logoutpage"),
    path('QuizzList', views.Quizzlistpage, name="Quizzlistpage"),
    path('Categorielistpage', views.Categorielistpage, name="Categorielistpage"),
    path('QuizzCreation', views.Quizzcreationpage, name="Quizzcreationpage"),
    path('QuestionAjout', views.QuestionAjoutpage, name="QuestionAjoutpage"),
    path('QuizzDetails/<int:quizz_id>', views.QuizzDetails, name="QuizzDetails"),
    path('QuizzCatelistpage/<int:categorie_id>', views.QuizzCatelistpage, name="QuizzCatelistpage")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 