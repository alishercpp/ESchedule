from django.contrib import admin
from .models import (
    School,
    Class,
    Student,
    Subject,
    Grade,
    Date,
    Schedule
)

admin.site.register(School)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)
admin.site.register(Date)
admin.site.register(Schedule)


