from django.urls import path
from unicodedata import name
from app import views



urlpatterns = [
path('',views.ens,name="enspage"),
path('etupage/', views.etu, name='etupage'),
path('classpage/', views.cla, name='classpage'),
path('search/',views.search,name='search'),
path('delete/<str:Matricule>/',views.delete_data,name="deletedata"),
path('<str:Matricule>/',views.update_data, name="updatedata"),
]
