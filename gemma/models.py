from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime





# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username


class Producers(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.IntegerField(default=0)
    city = models.CharField(max_length=200)
    phone = models.IntegerField(default=0)
    phones = models.IntegerField(default=0)
    fax = models.IntegerField(default=0)
    email = models.EmailField(max_length=200)


    def __unicode__(self):
        return self.name

class Resellers(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.IntegerField(default=0)
    city = models.CharField(max_length=200)
    phone = models.IntegerField(default=0)
    phones = models.IntegerField(default=0)
    fax = models.IntegerField(default=0)
    email = models.EmailField(max_length=200)
    producers = models.ManyToManyField(Producers)

    def __unicode__(self):
        return self.name

# Main List of items
class PricelistMain(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, blank=True)


    def __unicode__(self):
        return self.name


#List of Files in the items
class Pricelist(models.Model):
    pricelist_name = models.CharField(max_length=200)
    pricelist_detail = models.FileField(upload_to='media/%y/%m/%d')
    created = models.DateTimeField(auto_now_add=True, blank=True)
    pricelist_main = models.ForeignKey(PricelistMain)

    def __unicode__(self):
        return self.pricelist_name


#Main list of promotional material
class PromotionalMain(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, blank=True)


    def __unicode__(self):
        return self.name




#List of  files in promotional
class Promotional(models.Model):
   promotional_name = models.CharField(max_length=200)
   promotional_detail = models.FileField(upload_to='media/%y/%m/%d')
   created = models.DateTimeField(auto_now_add=True, blank=True)
   promotional_main = models.ForeignKey(PromotionalMain)



   def __unicode__(self):
       return self.promotional_name




