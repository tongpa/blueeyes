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

    print page
    print request
    print request.body
    orderType = OrderType.objects.filter(active__exact=True)
    rderType_json = serializers.serialize("json", orderType)

    return JsonResponse(rderType_json, safe=False)

def ordertypeparam(request):
    query = request.GET
    orderType = OrderType.objects.filter(active__exact = True)
    orderType_json = serializers.serialize("json", orderType)

    data = {}
    data['something'] = orderType_json
    #return JsonResponse(data)
    return HttpResponse(orderType_json, content_type='application/json; charset=UTF-8')

def listExpend(request, page):

    data = []
    data.append({'id':10, 'engine': 'Trident', 'browser':'Internet Explorer 4.0', 'platform':'Win 95+', 'version':'4', 'grade':'A'})
    data.append(
        {'id': 1, 'engine': 'Trident', 'browser': 'Internet Explorer 4.0', 'platform': 'Win 95+', 'version': '4',
         'grade': 'A'})
    data.append(
        {'id': 2, 'engine': 'Trident', 'browser': 'Internet Explorer 4.0', 'platform': 'Win 95+', 'version': '4',
         'grade': 'A'})
    data.append(
        {'id': 3, 'engine': 'Trident', 'browser': 'Internet Explorer 4.0', 'platform': 'Win 95+', 'version': '4',
         'grade': 'A'})
    data.append(
        {'id': 4, 'engine': 'Trident', 'browser': 'Internet Explorer 4.0', 'platform': 'Win 95+', 'version': '4',
         'grade': 'A'})
    data.append(
        {'id': 5, 'engine': 'Trident', 'browser': 'Internet Explorer 4.0', 'platform': 'Win 95+', 'version': '4',
         'grade': 'A'})
    data.append(
        {'id': 6, 'engine': 'Trident', 'browser': 'Internet Explorer 4.0', 'platform': 'Win 95+', 'version': '4',
         'grade': 'A'})
    data.append(
        {'id': 7, 'engine': 'Trident', 'browser': 'Internet Explorer 4.0', 'platform': 'Win 95+', 'version': '4',
         'grade': 'A'})
    data.append(
        {'id': 8, 'engine': 'Trident', 'browser': 'Internet Explorer 4.0', 'platform': 'Win 95+', 'version': '4',
         'grade': 'A'})
    data.append(
        {'id': 9, 'engine': 'Trident', 'browser': 'Internet Explorer 4.0', 'platform': 'Win 95+', 'version': '4',
         'grade': 'A'})
    #value = dict(draw= 1, recordsTotal = 10, recordsFiltered =30 ,data = data)
    value = dict(draw=1, recordsTotal=20, recordsFiltered=30, data=data)
    return JsonResponse(value, safe=False)