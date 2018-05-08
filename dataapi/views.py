# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.core import serializers

from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from signup.models import OrderType

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def ordertype(request, page):
    data = {}
    data['something'] = 'useful'
    print page
    print request
    print request.body
    return JsonResponse(data)

def ordertypeparam(request):
    query = request.GET
    orderType = OrderType.objects.filter(active__exact = True)
    orderType_json = serializers.serialize("json", orderType)

    data = {}
    data['something'] = orderType_json
    return JsonResponse(data)
    #return HttpResponse(orderType_json, content_type='application/json; charset=UTF-8')
