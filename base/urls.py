from django.urls import path 
from .views import MemberList, MemberCreate 

urlpatterns = [
    path('', MemberList.as_view(), name = 'members'),
    path('member-create/', MemberCreate.as_view(), name = 'member-create'),

]