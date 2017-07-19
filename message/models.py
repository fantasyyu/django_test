# _*_ coding:utf-8 _*_
from django.db import models

# Create your models here.
class UserMessage(models.Model):
    object_id = models.CharField(primary_key=True,default="", verbose_name="MainKey", max_length=50)
    name = models.CharField(max_length=20, verbose_name=u"Username", null=True, blank=True, default="")
    email = models.EmailField(verbose_name=u"emailaddress")
    address = models.CharField(max_length=100, verbose_name=u"address")
    message = models.CharField(max_length=500, verbose_name=u"information")

    class Meta:
        verbose_name = u"User Message"
        verbose_name_plural = verbose_name

