from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length = 100)

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    createur = models.ForeignKey(User, on_delete=models.CASCADE)

class Reponse(models.Model):
    reponse_text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reponse_valeur = models.BooleanField()
