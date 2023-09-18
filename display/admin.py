from django.contrib import admin
from .models import *

@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['tid', 'first_name', 'last_name', 'middle_name']

@admin.register(School)
class SchoolModelAdmin(admin.ModelAdmin):
    list_display = ['sid', 'name', 'rector']

@admin.register(Class)
class ClassModelAdmin(admin.ModelAdmin):
    list_display = ['cid', 'name', 'school', 'teacher']

@admin.register(Pupil)
class PupilModelAdmin(admin.ModelAdmin):
    list_display = ['pid', 'first_name', 'last_name', 'middle_name', 'phone_number'] 

@admin.register(Grade)
class GradeModelAdmin(admin.ModelAdmin):
    list_display = ['subject', 'teacher', 'sinf', 'maktab']

    def sinf(self, obj):
        return obj.subject.klass.name
    
    def maktab(self, obj):
        return obj.subject.klass.school.name
    
    def teacher(self, obj):
        return obj.subject.teacher
    

@admin.register(Subject)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ['sbid', 'name', 'teacher', 'klass', 'maktab']

    def maktab(self, obj):
        return obj.klass.school.name
