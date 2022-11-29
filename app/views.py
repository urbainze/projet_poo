from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import StudentRegistration,teacherRegistration , classRegistration
from .models import  Enseignant, CLASS, Etudiant
from django.db.models import Q


def first(request):
    return render(request,'base1.html')

def log0(request):
    return render(request,'login0.html')

def log1(request):
    return render(request,'login1.html')

def log2(request):
    return render(request,'login2.html')


# Create your views here.
#this function helps us to add data in our tables 
def ens(request):
    if request.method =='POST':
        fk = teacherRegistration(request.POST)
        if fk.is_valid():
            nn = fk.cleaned_data['Name']
            sn = fk.cleaned_data['Surname']
            mt = fk.cleaned_data['Matricule']
            em = fk.cleaned_data['Email']
            db = fk.cleaned_data['date_birth']
            pb = fk.cleaned_data['place_birth']
            cl = fk.cleaned_data['classe']
            nm = fk.cleaned_data['number']
            reg1 = Enseignant(Name = nn,Surname=sn,Matricule=mt,Email=em,date_birth=db,place_birth=pb,number=nm,classe=cl)
            reg1.save()
            fk = teacherRegistration()
    else:
        fk = teacherRegistration()
    return render(request,'enspage.html',{'form2':fk})

def etu(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm1 = fm.cleaned_data['Name']
            sn1 = fm.cleaned_data['Surname']
            mt1 = fm.cleaned_data['Matricule']
            em1 = fm.cleaned_data['Email']
            db1 = fm.cleaned_data['date_birth']
            pb1 = fm.cleaned_data['place_birth']
            cl1 = fm.cleaned_data['classe']
            reg = Etudiant(Name = nm1,Surname=sn1,Matricule=mt1,Email=em1,date_birth=db1,place_birth=pb1,classe=cl1)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request,'etupage.html',{'form':fm})




def cla(request):
    if request.method =='POST':
        fp = classRegistration(request.POST)
        if fp.is_valid():
            kl = fp.cleaned_data['nom_classe']
            pk = CLASS(nom_classe=kl)
            pk.save()
            fp = classRegistration()   
    else:
        fp = classRegistration()
    return render(request,'classpage.html',{'form3':fp})


#fonction pour chercher les éléments dans la base de donnée
def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        #data = Etudiant.objects.filter(classe__nom_classe__icontains=q).classe
        data = Etudiant.objects.filter(Q(classe__nom_classe__icontains = Etudiant.objects.filter(Matricule__icontains=q).values('classe'))|Q(classe__nom_classe__icontains=q))
    else:
        data = Etudiant.objects.all()
    context = {
        'data':data
    }
    return render(request,'search.html',context)

#fonction pour mettre à jour les données
def update_data(request,Matricule):
    if request.method == 'POST':
        pi = Etudiant.objects.get(pk=Matricule)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Etudiant.objects.get(pk=Matricule)
        fm = StudentRegistration(instance=pi)
    return render(request,'update.html', {'form8':fm})
    

#fonction pour supprimer des éléments dans la base de donnée
def delete_data(request,Matricule):
    if request.method=='POST':
        pi = Etudiant.objects.get(pk = Matricule)
        pi.delete()
        return redirect('search')

def search1(request):
    if 'p' in request.GET:
        p = request.GET['p']
        #data = Etudiant.objects.filter(classe__nom_classe__icontains=q).classe
        data = Etudiant.objects.filter(Matricule__icontains=p)
        if data is not None:
            return redirect('enspage')
        else:
            messages.error(request, "Please provide a valid Matricul.")
    return render(request,'login1.html')
