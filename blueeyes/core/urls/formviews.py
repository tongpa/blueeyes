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
from blueeyes.core.form.formexpend import PostForm

def listexpend(request):
    return render(request, 'formexpend.html')


def saveexpend(request):

    if request.method == "POST":
        formData = PostForm(request.POST)
        if formData.is_valid():
            post = formData.save(commit=False)
            print post.description
            post.save()
    return render(request, 'formexpend.html')

