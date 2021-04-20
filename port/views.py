from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return redirect('/home')

def home(request):
    return render(request, 'home.html')

def jdoe(request):
    return render(request, 'jdoe.html')

def python(request):
    return render(request, 'python.html')

def resume(request):
    return render(request, 'resume.html')