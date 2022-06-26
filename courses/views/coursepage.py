from django.shortcuts import render
from courses.models import Course

# Create your views here.

def coursePage(request, slug):
    course = Course.objects.get(slug = slug)
    context = {'course':course}
    return render(request, 'courses/course_page.html',context)