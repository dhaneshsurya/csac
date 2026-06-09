from django.contrib import admin
from .models import StudentFeedback, ParentFeedback, FacultyFeedback, AlumniFeedback


@admin.register(StudentFeedback)
class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'program', 'academic_year', 'overall_experience', 'submitted_at')
    list_filter = ('academic_year', 'program')
    search_fields = ('student_name', 'roll_number')
    readonly_fields = ('submitted_at',)


@admin.register(ParentFeedback)
class ParentFeedbackAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'student_name', 'academic_year', 'overall_satisfaction', 'submitted_at')
    list_filter = ('academic_year',)
    search_fields = ('parent_name', 'student_name')
    readonly_fields = ('submitted_at',)


@admin.register(FacultyFeedback)
class FacultyFeedbackAdmin(admin.ModelAdmin):
    list_display = ('faculty_name', 'department', 'academic_year', 'overall_satisfaction', 'submitted_at')
    list_filter = ('academic_year', 'department')
    search_fields = ('faculty_name', 'department')
    readonly_fields = ('submitted_at',)


@admin.register(AlumniFeedback)
class AlumniFeedbackAdmin(admin.ModelAdmin):
    list_display = ('alumni_name', 'batch_year', 'program', 'overall_experience', 'submitted_at')
    list_filter = ('batch_year',)
    search_fields = ('alumni_name', 'program')
    readonly_fields = ('submitted_at',)
