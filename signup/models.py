# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import  timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ExpenditureType(models.Model):
    id_expenditure_type = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=500, blank=True)
    active = models.BooleanField(max_length=1, default=1,blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class OrderType(models.Model):
    id_order_type = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=500, blank=True)
    active = models.BooleanField(max_length=1, default=1, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class ListExpenditure(models.Model):
    id_list_expenditure = models.IntegerField(primary_key=True)
    detail = models.TextField(max_length=500, blank=True)
    description = models.TextField(max_length=500, blank=True)
    id_order_type = models.ForeignKey(OrderType, on_delete=models.CASCADE)
    active = models.BooleanField(max_length=1, default=1, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)