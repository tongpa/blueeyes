# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
from django.views import generic
from blueeyes.core.form.formexpend import OrderExpendForm
@login_required
def listexpend(request):
    return render(request, 'formlistexpend.html')

def editexpend(request):
    return render(request, 'formexpend.html')
@login_required
def saveexpend(request):

    if request.method == "POST":
        formData = OrderExpendForm(request.POST)
        if formData.is_valid():
            post = formData.save(commit=False)
            print post.description
            print post.number
            print post.detail
            print post.id_order_type
            post.owner = request.user
            post.save()
    return render(request, 'formexpend.html')

