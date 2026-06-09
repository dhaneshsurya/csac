from django import forms
from .models import Department, DepartmentFaculty, DepartmentBanner, Program

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 8}),
            'hod_message': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput) and field_name not in ['hod_photo', 'banner_image']:
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class DepartmentFacultyForm(forms.ModelForm):
    class Meta:
        model = DepartmentFaculty
        fields = ['department', 'name', 'designation', 'qualification', 'specialization', 'photo', 'email', 'phone', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'vTextField form-control', 'placeholder': 'Enter full name'}),
            'designation': forms.TextInput(attrs={'class': 'vTextField form-control', 'placeholder': 'e.g. Assistant Professor, Professor'}),
            'qualification': forms.TextInput(attrs={'class': 'vTextField form-control', 'placeholder': 'e.g. M.Sc., Ph.D.'}),
            'specialization': forms.TextInput(attrs={'class': 'vTextField form-control', 'placeholder': 'e.g. Entomology, Organic Chemistry'}),
            'email': forms.EmailInput(attrs={'class': 'vTextField form-control', 'placeholder': 'e.g. faculty@chaitanyacg.ac.in'}),
            'phone': forms.TextInput(attrs={'class': 'vTextField form-control', 'placeholder': 'e.g. +91-XXXXXXXXXX'}),
        }


class DepartmentBannerForm(forms.ModelForm):
    class Meta:
        model = DepartmentBanner
        fields = ['department', 'image', 'caption', 'order']
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'vTextField form-control', 'placeholder': 'e.g. Zoology Lab Banner'}),
            'order': forms.NumberInput(attrs={'class': 'vIntegerField form-control', 'placeholder': '0'}),
        }


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        widgets = {
            'eligibility': forms.Textarea(attrs={'rows': 3}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()



