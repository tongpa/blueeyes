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
from signup import views
from blueeyes.core.urls import formviews

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^admin/', admin.site.urls),
    url('sample/', views.sample, name='sample'   ),
    url('forms/', views.forms, name='forms'   ),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),# see to app
    url(r'^signup/(?P<id>[0-9]+)/$', views.user, name='user'),# see to app
    url(r'^user/$', views.user, name='user'),# see to app
    url(r'^listexpend/$', formviews.listexpend, name ='listexpend'),
    url(r'^listexpend/edit/$', formviews.editexpend, name ='editexpend'),
    url(r'^listexpend/save/$', formviews.saveexpend, name ='saveexpend'),
    url(r'^api/', include('dataapi.urls')),
    #url(r'^(?P<id>[0-9]+)/$', views.user, name='user'),
    #url('signup/', include('signup.urls'))
]
