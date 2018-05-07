# -*- coding: utf-8 -*-
from django import forms
from signup.models import ExpenditureType
class PostForm(forms.ModelForm):

    class Meta:
        model = ExpenditureType
        fields = ('description',)