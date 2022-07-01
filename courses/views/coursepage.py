from django.shortcuts import render,HttpResponse, redirect
from courses.models import Course, Video


# Create your views here.

def coursePage(request, slug):
    course = Course.objects.get(slug = slug)
    print(request.user.is_authenticated)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")
    if serial_number is None:
        serial_number=1
    video = Video.objects.get(course=course, serial_number =serial_number)
    
    if (request.user.is_authenticated is False) and (video.is_preview is False):
        return redirect('login')
    
    context = {'course':course, 'video':video, 'videos':videos}
    return render(request, 'courses/course_page.html',context)
   