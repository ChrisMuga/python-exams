from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#home
def home(request):
    return render(request,'home.html', {'title':'Home'})

#register
def register(request):
    return render(request, 'register.html', {'title': 'Register'})

#new-user
def new_user(request):
    return HttpResponse(request.POST)