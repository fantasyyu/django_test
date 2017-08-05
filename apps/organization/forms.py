# _*_ coding:utf-8 _*_

from django.forms import forms

from operation.models import UserAsk

class UserAskForm(forms.Modelforms):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

