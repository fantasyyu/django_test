# _*_ coding:utf-8 _*_

from django import forms

from captcha.fields import CaptchaField
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=4)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=4)
    captcha = CaptchaField(error_messages={"invalid":u"验证码error"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码error"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=4)
    password2 = forms.CharField(required=True, min_length=4)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'birday', 'gender', 'address', 'mobile',]
