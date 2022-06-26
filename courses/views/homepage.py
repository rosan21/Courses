from django.shortcuts import render
from courses.models import Course

# Create your views here.

def home(request):
    courses = Course.objects.all() 
    
    return render(request, 'courses/home.html', context= {'courses':courses})