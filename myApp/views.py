from django.shortcuts import render
from django.http import HttpResponse
from .models import News
# Create your views here.


def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Main page'
    }
    return render(request, 'myApp/home.html', data)


def contacts(request):
    return render(request, 'myApp/contacts.html', {'title': 'Contacts page'})