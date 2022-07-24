from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.teamList, name = 'team')

]