from __future__ import unicode_literals
from django.db import models

from rest_framework.authtoken.models import Token
from django.conf import settings

class Company_Crunchbase(models.Model):
    name =  models.TextField(max_length=50,primary_key=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    rank = models.TextField(max_length=300, null=True, blank=True)
    category = models.TextField(max_length=300, null=True, blank=True)
    location = models.TextField(max_length=300, null=True, blank=True)
    website = models.TextField(max_length=300, null=True, blank=True)
    facebook = models.TextField(max_length=300, null=True, blank=True)
    twitter = models.TextField(max_length=300, null=True, blank=True)
    linkdin = models.TextField(max_length=300, null=True, blank=True)
    phone= models.TextField(max_length=300, null=True, blank=True)
    email = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):  # __unicode__ on Python 2

        return self.name+" , "+self.rank



class People_Crunchbase(models.Model):
    name =  models.TextField(max_length=50,primary_key=True)
    company_name= models.TextField(max_length=50, null=True, blank=True)
    gender = models.TextField(max_length=10, null=True, blank=True)
    designation = models.TextField(max_length=300, null=True, blank=True)
    first_name = models.TextField(max_length=300, null=True, blank=True)
    last_name = models.TextField(max_length=300, null=True, blank=True)
    rank = models.TextField(max_length=300, null=True, blank=True)
    twitter = models.TextField(max_length=300, null=True, blank=True)
    linkdin = models.TextField(max_length=300, null=True, blank=True)
    facebook = models.TextField(max_length=300, null=True, blank=True)
    location = models.TextField(max_length=300, null=True, blank=True)
    biography = models.TextField(max_length=500, null=True, blank=True)





    def __str__(self):  # __unicode__ on Python 2

        return self.name+" , "+self.company_name




