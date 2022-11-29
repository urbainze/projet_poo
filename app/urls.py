from django.urls import path
from unicodedata import name
from app import views



urlpatterns = [
path('',views.first,name="firstpage"),
path('login0/',views.log0,name="login0"),
path('login1/',views.log1,name="login1"),
path('login2/',views.log2,name="login2"),
path('enspage/',views.ens,name="enspage"),
path('etupage/', views.etu, name='etupage'),
path('classpage/', views.cla, name='classpage'),
path('search/',views.search,name='search'),
path('login1/',views.search1,name='search1'),
path('delete/<str:Matricule>/',views.delete_data,name="deletedata"),
path('<str:Matricule>/',views.update_data, name="updatedata"),
]
