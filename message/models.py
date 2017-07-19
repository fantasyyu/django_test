from django.db import models

# Create your models here.
class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"Username")
    email = models.EmailField(verbose_name=u"emailaddress")
    address = models.CharField(max_length=100, verbose_name=u"address")
    message = models.CharField(max_length=500, verbose_name=u"information")

    class Meta:
        verbose_name = u"user message"

