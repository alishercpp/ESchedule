from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import (
    Schedule,
    School,
    Student,
    Subject,
    Class,
    Grade,
)
from .serializers import (
    SchoolSerailizer,
    StudentSerializer,
    SubjectSerializer,
    ScheduleSerializer,
    ClassSerializer,
    GradeSerializer,
)


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerailizer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get']

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get']

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get']

class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get']

class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get']

class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['post']
