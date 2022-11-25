from django.contrib import admin
from .models import CLASS,Etudiant, Enseignant
# Register your models here.


@admin.register(CLASS)
class classeAdmin(admin.ModelAdmin):
    list_display = ['nom_classe']

@admin.register(Etudiant)
class classeAdmin(admin.ModelAdmin):
    list_display = ['Matricule','Name','Surname','Email','place_birth','date_birth','classe']


@admin.register(Enseignant)
class classeAdmin(admin.ModelAdmin):
    list_display = ['Matricule','Name','Surname','Email','place_birth','date_birth','number','classe']
