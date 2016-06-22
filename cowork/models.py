from __future__ import unicode_literals
from django.core.validators import RegexValidator
#from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime as dt

def upload_logo(company, filename):
    return "%s/%s" %(company.user.id, filename)

class Company(models.Model):
    user = models.ForeignKey('accounts.User',
                             related_name='companies')
    name = models.CharField(max_length=100, unique=True)
    vat_id = models.CharField(max_length=10,
                              validators=[RegexValidator(r'^\d{10}$')],
                              verbose_name='VAT-ID', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to = upload_logo,
                            null=True,
                            blank=True,
                            width_field="width_field",
                            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class LocationManager(models.Manager):
    def get_queryset(self):
        free_desks = total_desks - reserved_desks
        return super(LocationManager, self).get_queryset().filter(free_desks__gt=0)
    
class Location(models.Model):
    company = models.ForeignKey('Company',
        related_name='locations')
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=6, validators=[RegexValidator(r'^\d\d-\d\d\d$')], blank=True, null=True)
    #geolocation = models.PointField(null=True, blank=True)
    total_desks = models.IntegerField(verbose_name='Total desks')
    reserved_desks = models.IntegerField(verbose_name='Reserved desks')
    price = models.DecimalField(verbose_name='Price per desk $',
        max_digits=12, decimal_places=2)
    objects = models.Manager()
    free_objects = LocationManager()

    def __str__(self):
        return '%s, %s' % (self.company, self.city)

    @property
    def free_desks(self):
        return self.total_desks - self.reserved_desks

    def reserve_desk(self):
        self.reserved_desks += 1

    def clean(self):
        if self.reserved_desks and self.total_desks:
         if self.reserved_desks > self.total_desks:
             raise ValidationError('Must be less than total number of desks.')


class Desk(models.Model):
    owner = models.ForeignKey('accounts.User', related_name='owner',
        null=True)
    location = models.ForeignKey(Location, related_name='location')
    rent_start_date = models.DateTimeField(default=timezone.now)
    rent_end_date = models.DateTimeField(default = timezone.now() + timezone.timedelta(days=30))
    
    def __str__(self):
        return '%s' % self.location.company.name
    
    def days_of_rent(self):
        # calculates total number of days of rent
        return (self.rent_end_date - self.rent_start_date).days
    
    def final_price(self):
        # calculates final price for desk for indicated period
        return self.days_of_rent() * self.location.price
    
    def clean(self):
        if self.rent_end_date and self.rent_start_date:
            delta = (self.rent_end_date - self.rent_start_date).days
            if delta <= 0:
                raise ValidationError('Incorrent dates.')
