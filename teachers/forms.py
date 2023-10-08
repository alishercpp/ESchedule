from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Teacher


class TeacherCreationForm(UserCreationForm):

    class Meta:
        model = Teacher
        fields = ("username", "first_name", "last_name", "middle_name")

class TeacherChangeForm(UserChangeForm):

    class Meta:
        model = Teacher
        fields = ("first_name", "last_name", "middle_name")