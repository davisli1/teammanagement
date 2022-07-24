from django.shortcuts import render
from django.views.generic.list import ListView


from .models import Member

class MemberList(ListView):
    model = Member
    context_object_name = 'members'

