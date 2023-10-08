from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import TeacherCreationForm, TeacherChangeForm
from .models import Teacher


class TeacherAdmin(UserAdmin):
    add_form = TeacherCreationForm
    form = TeacherChangeForm
    model = Teacher
    list_display = ("username", "first_name", "last_name", "middle_name")
    fieldsets = (
        ("O'qituvchini tahrirlash", {"fields": ("first_name", "last_name", "middle_name")}),
    )
    add_fieldsets = (
        ("Yangi o'qituvchi qo'shish", {
            "classes": ("wide", ),
            "fields": (
                "password1", "password2",
                "first_name", "last_name", "middle_name"
            ),
        }),
    )
    search_fields = ("username", "first_name", "last_name", "middle_name")
    ordering = ("username",)

admin.site.register(Teacher, TeacherAdmin)