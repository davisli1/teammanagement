from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy    


from .models import Member

class MemberList(ListView):
    model = Member
    context_object_name = 'members'

class MemberCreate(CreateView):
    model = Member
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'admin']
    success_url = reverse_lazy('members')
    template_name = 'base/member_create.html'

class MemberUpdate(UpdateView):
    model = Member
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'admin']
    success_url = reverse_lazy('members')
    template_name = 'base/member_update.html'
