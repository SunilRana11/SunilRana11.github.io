from django.contrib import admin

from .models import Result, Teacher, Student

# Register your models here.


admin.site.register(Teacher)
admin.site.register(Result)
admin.site.register(Student)