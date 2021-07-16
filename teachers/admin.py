from django.contrib import admin
from teachers.models import Teacher
from teachers.filters import SubjectsTaughtFilter, LastNameFilter


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'room_number', 'subjects_taught')
    list_filter = (SubjectsTaughtFilter, LastNameFilter)

