from django.contrib import admin

from .models import Categorie, Quizz, Question, Reponse

# Register your models here.

admin.site.register(Categorie)
admin.site.register(Quizz)
admin.site.register(Question)
admin.site.register(Reponse)
