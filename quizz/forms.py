from django import forms

from quizz.models import Categorie

class SignInForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

    def clean(self):
        cleaned_data = super(SignInForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not username and not password:
            raise forms.ValidationError('Vous devez rentrer vos informations')

class AuthenticateForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

    def clean(self):
        cleaned_data = super(AuthenticateForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if not username and not password:
            raise forms.ValidationError('Vous devez rentrer vos informations')

class QuizzCreationForm(forms.Form):
    nom = forms.CharField(max_length=200)
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all().order_by('nom'))

    def clean(self):
        cleaned_data = super(QuizzCreationForm, self).clean()
        nom = cleaned_data.get('nom')
        categorie = cleaned_data.get('categorie')
        if not nom and not categorie:
            raise forms.ValidationError('Vous devez rentrer vos informations')