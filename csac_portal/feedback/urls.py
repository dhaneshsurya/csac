from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('student/', views.student_feedback, name='student_feedback'),
    path('parent/', views.parent_feedback, name='parent_feedback'),
    path('faculty/', views.faculty_feedback, name='faculty_feedback'),
    path('alumni/', views.alumni_feedback, name='alumni_feedback'),
]
