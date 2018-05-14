# -*- coding: utf-8 -*-
from django import forms
from signup.models import ExpenditureType, ListExpenditure
class PostForm(forms.ModelForm):

    class Meta:
        model = ExpenditureType
        fields = ('description',)

class OrderExpendForm(forms.ModelForm):

    class Meta:
        model = ListExpenditure
        fields = ('description','detail', 'id_order_type', 'number')