from django.contrib import admin
from django.urls import path, include
from teachers.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('schools.urls')),
    path('login/', login, name='login'),
]
