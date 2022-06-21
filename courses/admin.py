from django.contrib import admin
from courses.models import Course, Tag, Learning, Prerequisite

# Register your models here.

admin.site.register(Course)
admin.site.register(Tag)
admin.site.register(Learning)
admin.site.register(Prerequisite)
