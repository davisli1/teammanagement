from django.urls import path 
from .views import MemberList, MemberCreate, MemberUpdate   

urlpatterns = [
    path('', MemberList.as_view(), name = 'members'),
    path('member-create/', MemberCreate.as_view(), name = 'member-create'),
    path('member-update/<int:pk>/', MemberUpdate.as_view(), name = 'member-update'),

]