from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Company(models.Model):
    user = models.ForeignKey('accounts.User',
                             related_name='companies')
    name = models.CharField(max_length=100)
    vat_id = models.CharField(max_length=10,
                              validators=[RegexValidator(r'^\d{10}$')],
                              verbose_name='VAT-ID', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to = 'logo',
                            null=True,
                            blank=True,
                            width_field="width_field",
                            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    company = models.ForeignKey('Company',
        related_name='locations')
    city = models.CharField(max_length=200)
    #address = models.CharField(max_length=50)
    #postal_code = models.CharField(max_length=6, validators=[RegexValidator(r'^\d\d-\d\d\d$')])
    total_desks = models.IntegerField(verbose_name='Total desks')
    reserved_desks = models.IntegerField(verbose_name='Reserved desks')
    price = models.DecimalField(verbose_name='Price per desk $',
        max_digits=12, decimal_places=2)

    def __unicode__(self):
        return '%s' % (self.city)

    @property
    def free_desks(self):
        return self.total_desks - self.reserved_desks


class Desk(models.Model):
    owner = models.OneToOneField('accounts.User', related_name='desks',
        null=True)
    location = models.OneToOneField(Location, related_name='desks')
    rent_start_date = models.DateTimeField(null=True)
    rent_end_date = models.DateTimeField(null=True)
    
    def __unicode__(self):
        return '%s' % self.location
