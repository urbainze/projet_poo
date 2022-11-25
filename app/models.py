from django.db import models

# Create your models here.

class user(models.Model):
    Name = models.CharField(max_length=70)
    Matricule = models.CharField(max_length=10,primary_key=True)
    Surname = models.CharField(max_length=70)
    place_birth = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    date_birth = models.DateField(max_length=12)


class CLASS(models.Model):
    nom_classe = models.CharField(max_length=30,primary_key=True)

    def __str__(self):
        return self.nom_classe


class Etudiant(user):
    classe = models.ForeignKey(CLASS,on_delete=models.CASCADE)

    def __str__(self):
        return self.classe




class Enseignant(user):
    number = models.CharField(max_length=20)
    classe = models.ForeignKey(CLASS,on_delete=models.CASCADE)

    def __str__(self):
        return self.classe