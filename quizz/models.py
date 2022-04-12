from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.nom

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    createur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class Reponse(models.Model):
    reponse_text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    reponse_valeur = models.BooleanField()

    def __str__(self):
        return self.reponse_text
