# -*- coding: utf-8 -*-
"""blueeyes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ordertype/(?P<page>[0-9]+)/$', views.ordertype, name='index'),  #กำหมดค่า path ข้างหลังเลยว่าเป็นตัวเลข แบบ /10
    url(r'^ordertypeparam/$', views.ordertypeparam, name='index'),  #ไม่สนในว่า path ข้างหลังจะเป็นอะไรใช้ทำหรับทำ paramiter แบบ ?page=1&limit=10

]
