from django.shortcuts import render
from django.http import HttpResponse

def teamList(request):
    return HttpResponse('Team Management')

