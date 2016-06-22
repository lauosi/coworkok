from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
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
        """
        Without data
        """
        form_data = {}
        form = CompanyCreationForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_location_without(self):
        """
        Without data
        """
        form_data = {}
        form = LocationCreationForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_renting_desk_without(self):
        """
        Without data
        """
        form_data = {}
        form = RentingDeskForm(data=form_data)
        self.assertEqual(form.is_valid(), False)
        
    def test_location_reserved(self):
        """
        Location with more reserved desks than total desks.
        """
        form_data = {'city': 'Wrocław', 'total_desks': 10, 'reserved_desks': 15, 'price': 5.0}
        form = LocationCreationForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_renting_desks(self):
        """
        Rent end date is sooner than rent start date.
        """
        rent_start_date = timezone.now() + timedelta(days=30)
        rent_end_date = timezone.now()
        form_data = {'rent_start_date':rent_start_date, 'rent_end_date': rent_end_date}
        form = RentingDeskForm()
        self.assertEqual(form.is_valid(), False)
        
    def test_company_vat(self):
        """
        Company form with wrong VAT ID (must be: 10 digits)
        """
        form_data = {'name': 'Company1', 'vat_id': 123}
        form = CompanyCreationForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_location_postal_code(self):
        """
        Wrong postal code (must be in format 00-000)
        """
        form_data = {'city': 'Wrocław', 'postal_code': 1236,'total_desks': 10, 'reserved_desks': 15, 'price': 5.0}
        form = LocationCreationForm(data=form_data)
        self.assertEqual(form.is_valid(), False)



        
        
        
