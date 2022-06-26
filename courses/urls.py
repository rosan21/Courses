from django.urls import path
from courses.views import home, coursePage

urlpatterns = [
    path('', home, name ='homepage'),
    path('course/<str:slug>',coursePage, name='coursepage' )
]