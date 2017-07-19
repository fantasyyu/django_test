# _*_ coding:utf-8 _*_
from django.shortcuts import render
import MySQLdb
from .models import UserMessage
# Create your views here.
def get_form(request):
    # all_messages = UserMessage.objects.filter(name="yujian")
    # for message in all_messages:
    #     print(message.name)
    #     print(message.address)
    # user_message = UserMessage()
    # user_message.name = "jiajia"
    # user_message.address = "上海市嘉定区"
    # user_message.message = "yoyoyo"
    # user_message.email = "jia@126.com"
    # user_message.object_id = "234"
    # user_message.save()
    if request.method == 'POST':
        name = request.POST.get('name','')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.address = address
        user_message.message = message
        user_message.email = email
        user_message.object_id = "334"
        user_message.save()

    return render (request, 'messageform.html')