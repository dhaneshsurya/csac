from django import forms
from .models import StudentFeedback, ParentFeedback, FacultyFeedback, AlumniFeedback

RATING_WIDGET = forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)],
                             attrs={'class': 'form-select'})

YEAR_CHOICES = [(str(y), f"{y}-{y+1}") for y in range(2020, 2027)]


class StudentFeedbackForm(forms.ModelForm):
    class Meta:
        model = StudentFeedback
        fields = '__all__'
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control'}),
            'program': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_study': forms.Select(choices=[('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year')], attrs={'class': 'form-select'}),
            'academic_year': forms.Select(choices=YEAR_CHOICES, attrs={'class': 'form-select'}),
            'teaching_quality': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'infrastructure': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'library_resources': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'sports_facilities': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'overall_experience': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'suggestions': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class ParentFeedbackForm(forms.ModelForm):
    class Meta:
        model = ParentFeedback
        fields = '__all__'
        widgets = {
            'parent_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'program': forms.TextInput(attrs={'class': 'form-control'}),
            'academic_year': forms.Select(choices=YEAR_CHOICES, attrs={'class': 'form-select'}),
            'teaching_quality': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'communication': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'safety': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'overall_satisfaction': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'suggestions': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class FacultyFeedbackForm(forms.ModelForm):
    class Meta:
        model = FacultyFeedback
        fields = '__all__'
        widgets = {
            'faculty_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'academic_year': forms.Select(choices=YEAR_CHOICES, attrs={'class': 'form-select'}),
            'infrastructure': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'admin_support': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'research_support': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'work_environment': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'overall_satisfaction': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'suggestions': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class AlumniFeedbackForm(forms.ModelForm):
    class Meta:
        model = AlumniFeedback
        fields = '__all__'
        widgets = {
            'alumni_name': forms.TextInput(attrs={'class': 'form-control'}),
            'batch_year': forms.NumberInput(attrs={'class': 'form-control', 'min': 2001}),
            'program': forms.TextInput(attrs={'class': 'form-control'}),
            'current_status': forms.TextInput(attrs={'class': 'form-control'}),
            'teaching_quality': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'campus_experience': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'career_support': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'overall_experience': forms.Select(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], attrs={'class': 'form-select'}),
            'suggestions': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
