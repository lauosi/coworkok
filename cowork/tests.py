from django.test import TestCase

from cowork.forms import CompanyCreationForm, LocationCreationForm, RentingDeskForm
from accounts.forms import UserCreationForm, LoginForm
from .models import Company, Location, Desk
from accounts.models import User

def create_user_coworker(email, password):
    return User.objects.create(user_type=0, email=email, password=password)

def create_user_company(email, password):
    return User.objects.create(user_type=1, email=email, password=password)

def create_company(name):
    user = create_user_company('company@gmail.com', 'password')
    return Company.objects.create(user=user, name=name)

class CreationFormTests(TestCase):
        
    def test_company_without(self):
        form_data = {}
        form = CompanyCreationForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_location_without_name(self):
        form_data = {'total_desks': 10, 'reserved_desks': 5}
        form = LocationCreationForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_renting_desk_without(self):
        form_data = {}
        form = RentingDeskForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_company_only_name(self):
        form_data = {'name': 'Company1'}
        form = CompanyCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_location_reserved1(self):
        """
        Location with less reserved desks than total desks.
        """
        form_data = {'city': 'Wrocław', 'total_desks': 10, 'reserved_desks': 5, 'price': 5.0}
        form = LocationCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_location_reserved2(self):
        """
        Location with more reserved desks than total desks.
        """
        form_data = {'city': 'Wrocław', 'total_desks': 10, 'reserved_desks': 15, 'price': 5.0}
        form = LocationCreationForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        
##    def test_location_free_desks(self):
##        company = create_company('Company')
##        location = Location(company=company, city="Wrocław", total_desks='10', free_desks='11', price='5.50')
##        
##        
