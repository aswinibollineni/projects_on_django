from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'myapp/home.html')

def contact_us(request):
    return render(request, 'myapp/contact_us.html')
