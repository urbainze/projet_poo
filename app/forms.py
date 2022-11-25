from django.core import validators
from django import forms
from django.forms import fields
from .models import  CLASS, Enseignant, Etudiant

"""class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['Matricule','Name','Surname','Email','place_birth','date_birth','classe']
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Matricule':forms.TextInput(attrs={'class':'form-control'}),
            'Surname':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'place_birth':forms.TextInput(attrs={'class':'form-control'}),
            'date_birth':forms.DateInput(attrs={'class':'form-control'}),
            'classe':forms.TextInput(attrs={'class':'form-control'})
        }
"""
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['Matricule','Name','Surname','Email','place_birth','date_birth','classe']
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Matricule':forms.TextInput(attrs={'class':'form-control'}),
            'Surname':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'place_birth':forms.TextInput(attrs={'class':'form-control'}),
            'date_birth':forms.DateInput(attrs={'class':'form-control'}),
            'classe':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'})
        }

class teacherRegistration(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['Matricule','Name','Surname','Email','place_birth','date_birth','number','classe']
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Matricule':forms.TextInput(attrs={'class':'form-control'}),
            'Surname':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'place_birth':forms.TextInput(attrs={'class':'form-control'}),
            'date_birth':forms.DateInput(attrs={'class':'form-control'}),
            'classe':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'})
        }

class classRegistration(forms.ModelForm):
    class Meta:
        model = CLASS
        fields = ['nom_classe']
        widgets = {
            'nom_classe':forms.TextInput(attrs={'class':'form-control'}),
            }


#class classeChangeListForm(forms.ModelForm):
    #classe = forms.ModelMultipleChoiceField(queryset=CLASS.objects.all(), required=False)