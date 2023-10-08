from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ScheduleViewSet,
    SchoolViewSet,
    StudentViewSet,
    SubjectViewSet,
    ClassViewSet,
    GradeViewSet,
)

router = DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'students', StudentViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]