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


def listexpend(request):
    return render(request, 'formexpend.html')

