from rest_framework import serializers
from .models import (
    School,
    Student,
    Schedule,
    Subject,
    Class,
    Grade
)

class SchoolSerailizer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["id", "sid", "name", "description", "region", "town", "direktor", "classes"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['klass', 'schedule']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'teacher', 'grades']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["id", "name", "teacher", "school", "subjects", "students", "schedule"]

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ["number", "subject", "student"]