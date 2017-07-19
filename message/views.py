from django.shortcuts import render
import MySQLdb

# Create your views here.
def get_form(request):
    return render(request, 'messageform.html')