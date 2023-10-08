from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from utils.generatos import generate

from .managers import TeacherManager

class Teacher(AbstractUser):
    username    = models.CharField(max_length=20, unique=True, null=False, blank=False, default=generate)
    first_name  = models.CharField(max_length=100, null=False, blank=False)
    last_name   = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=False, blank=False)
    objects     = TeacherManager()

    USERNAME_FIELD = 'username'


    def __str__(self):
        return self.username