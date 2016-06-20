from django import forms
from cowork.models import *
from django.contrib.admin import widgets

class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'vat_id', 'website', 'logo',)
        labels = {
            'name': 'Company name'
        }


class LocationCreationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('city', 'address', 'postal_code', 'total_desks', 'reserved_desks', 'price')


class RentingDeskForm(forms.ModelForm):
    class Meta:
        model = Desk
        fields = ('rent_start_date', 'rent_end_date')
