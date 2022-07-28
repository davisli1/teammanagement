from django.test import TestCase
from .models import Member
from django.urls import reverse, resolve
from .views import MemberList, MemberCreate, MemberDelete, MemberUpdate

# Testing URLs
class TestUrls(TestCase):
    def test_create_url_is_resolved(self):
        url = reverse('member-create')
        self.assertEquals(resolve(url).func.view_class, MemberCreate)

    def test_list_url_is_resolved(self):
        url = reverse('members')
        self.assertEquals(resolve(url).func.view_class, MemberList)

# Testing Model
class TestModel(TestCase):
    def setUp(self):
        self.member = Member.objects.create(
            first_name = 'Ted',
            last_name = 'Mosby',
            email = 'ted@hotmail.com',
            phone_number = '416-555-5555',
            admin = False
        )

    def test_first_name(self):
        self.assertEquals(self.member.first_name, 'Ted')

    def test_last_name(self):
        self.assertEquals(self.member.last_name, 'Mosby')

    def test_email(self):
        self.assertEquals(self.member.email, 'ted@hotmail.com')

    def test_phone_numer(self):
        self.assertEquals(self.member.phone_number, '416-555-5555')

    def test_admin(self):
        self.assertEquals(self.member.admin, False)