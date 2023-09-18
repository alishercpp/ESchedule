from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('school/<int:sid>/', school, name='school'),
    path('class/<int:cid>/', klass, name='class'),
    path('subject/<int:sbid>/', subject, name='subject'),
    path('save/<int:sbid>/', save, name='save')
]
