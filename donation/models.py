from django.db import models
from datetime import datetime,timedelta
from django import forms

class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_age = models.IntegerField()
    user_adhaar = models.BigIntegerField()
    user_email = models.EmailField(unique=True)
    user_blood = models.CharField(max_length=5 , blank=False)
    user_phone = models.CharField(max_length=20)
    '''
    The following 3 fields are for storing the location of the user precisely
    '''
    user_area = models.CharField(max_length=100)
    user_city = models.CharField(max_length=100)
    user_pin = models.IntegerField()

    def __str__(self):
        return self.user_name + '-' + self.user_blood

'''
Organs included:
1. Kidney
2. Heart
3. Lung
4. Eye

'''


class donor(models.Model):
    user_id = models.ForeignKey('user')
    donor_organ  = models.BooleanField(default=False)
    donor_blood = models.BooleanField(default = False)
    donor_kidney = models.BooleanField(default = False)
    donor_heart = models.BooleanField(default = False)
    donor_lung = models.BooleanField(default = False)
    donor_eye = models.BooleanField(default = False)


class needer(models.Model):
    user_id = models.ForeignKey('user')
    needer_organ = models.BooleanField(default=False)
    needer_blood = models.BooleanField(default = False)
    needer_kidney = models.BooleanField(default=False)
    needer_heart = models.BooleanField(default = False)
    needer_lung = models.BooleanField(default = False)
    needer_eye = models.BooleanField(default = False)
    '''
    The following 3 fields are for storing the location of the needer
    '''
    needer_area = models.CharField(max_length=100)
    needer_city = models.CharField(max_length=100)
    needer_pin = models.IntegerField()


class emergency(models.Model):
    user_id = models.ForeignKey('user')
    emer_blood = models.CharField(max_length=5)
    '''
    The following 3 fields are for storing the location of the emergency
    '''
    emer_area = models.CharField(max_length=100)
    emer_city = models.CharField(max_length=100)
    emer_pin = models.IntegerField()
    emer_start = models.DateTimeField(auto_now_add=True)
    '''
    emer_end = models.TimeField(auto_now_add=True) + timedelta(hours=24)
    if time.now > emer_end : then change status to "passive" and delete the entry from the database
    '''
    emer_status = models.CharField(default = "active", max_length=100)
