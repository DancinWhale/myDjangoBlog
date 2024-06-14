from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    news = [
        {
            'title': 'First title',
            'text': 'Full title text',
            'date': '10.06.2020',
            'author': 'Joanna'
        },
        {
            'title': 'Second title',
            'text': 'Full title text',
            'date': '30.08.2020'
        }
    ]
    data = {
        'news': news,
        'title': 'Main page'
    }
    return render(request, 'myApp/home.html', data)


def contacts(request):
    return render(request, 'myApp/contacts.html', {'title': 'Contacts page'})