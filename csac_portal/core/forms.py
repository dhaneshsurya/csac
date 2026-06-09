from django import forms
from .models import (
    SiteSettings, CareerGuidanceSubmission, AboutPage, Committee,
    CommitteeMember, CommitteeActivity, CommitteeGalleryImage,
    Policy, Notice, Event, UGCTable, UGCDocument,
    UGCPageSettings, UGCGrant, BreadcrumbSettings, PageBreadcrumb,
    NSSPageSettings, NSSActivity, NSSGalleryImage,
    IICPageSettings, IICGalleryImage
)

class CareerGuidanceForm(forms.ModelForm):
    class Meta:
        model = CareerGuidanceSubmission
        fields = ['fname', 'lname', 'email', 'phone', 'msg']
        widgets = {
            'fname': forms.TextInput(attrs={'id': 'fname', 'placeholder': 'First Name', 'required': True}),
            'lname': forms.TextInput(attrs={'id': 'lname', 'placeholder': 'Last Name', 'required': True}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Email..', 'required': True}),
            'phone': forms.TextInput(attrs={'id': 'Phone', 'placeholder': 'Phone', 'required': True, 'type': 'number'}),
            'msg': forms.Textarea(attrs={'id': 'msg', 'placeholder': 'Enter Your Comments'}),
        }


class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = '__all__'
        widgets = {
            'about_us_description_1': forms.Textarea(attrs={'rows': 4}),
            'about_us_description_2': forms.Textarea(attrs={'rows': 4}),
            'about_us_description_3': forms.Textarea(attrs={'rows': 4}),
            'mission_statement': forms.Textarea(attrs={'rows': 3}),
            'vision_text': forms.Textarea(attrs={'rows': 4}),
            'mission_text_1': forms.Textarea(attrs={'rows': 3}),
            'mission_text_2': forms.Textarea(attrs={'rows': 3}),
            'governance_text': forms.Textarea(attrs={'rows': 6}),
            'features_list': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Enter distinctive features, one per line...'}),
            'testimonial_text': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class CommitteeForm(forms.ModelForm):
    class Meta:
        model = Committee
        fields = ['name', 'slug', 'description', 'order']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class CommitteeMemberForm(forms.ModelForm):
    class Meta:
        model = CommitteeMember
        fields = ['committee', 'name', 'designation', 'role_in_committee', 'order']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class CommitteeActivityForm(forms.ModelForm):
    class Meta:
        model = CommitteeActivity
        fields = ['committee', 'title', 'description', 'date', 'image', 'order']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput) and field_name != 'image':
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class CommitteeGalleryImageForm(forms.ModelForm):
    class Meta:
        model = CommitteeGalleryImage
        fields = ['committee', 'image', 'caption', 'order']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput) and field_name != 'image':
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['title', 'document', 'document_url', 'description', 'order']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput) and field_name != 'document':
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'category', 'document', 'document_url', 'published_date', 'show_in_marquee', 'marquee_flag', 'is_active']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput) and field_name != 'document':
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'date', 'time', 'location', 'description', 
            'image', 'image_url', 'brochure', 'registration_link', 
            'youtube_url', 'link', 'is_active'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput) and field_name not in ['image', 'brochure']:
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class UGCTableForm(forms.ModelForm):
    class Meta:
        model = UGCTable
        fields = ['name', 'order', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class UGCDocumentForm(forms.ModelForm):
    class Meta:
        model = UGCDocument
        fields = ['ugc_table', 'sn', 'title', 'file', 'file_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput) and field_name != 'file':
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class UGCPageSettingsForm(forms.ModelForm):
    class Meta:
        model = UGCPageSettings
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'status_2f_12b_text': forms.Textarea(attrs={'rows': 4}),
            'benefits_list': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Enter benefits, one per line...'}),
            'autonomy_status_text': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class UGCGrantForm(forms.ModelForm):
    class Meta:
        model = UGCGrant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'
        widgets = {
            'google_maps_embed': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput) and field_name not in ['college_logo', 'college_logo_mobile', 'logo2', 'logo3', 'logo4', 'logo5']:
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class BreadcrumbSettingsForm(forms.ModelForm):
    class Meta:
        model = BreadcrumbSettings
        fields = ['default_image', 'default_image_url', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput,)) and field_name != 'default_image':
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class PageBreadcrumbForm(forms.ModelForm):
    class Meta:
        model = PageBreadcrumb
        fields = ['page_key', 'custom_image', 'custom_image_url', 'use_default', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput,)) and field_name != 'custom_image':
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class NSSPageSettingsForm(forms.ModelForm):
    class Meta:
        model = NSSPageSettings
        fields = '__all__'
        widgets = {
            'banner_description': forms.Textarea(attrs={'rows': 4}),
            'about_description': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput,)) and field_name not in ['banner_image', 'banner_icon']:
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class NSSActivityForm(forms.ModelForm):
    class Meta:
        model = NSSActivity
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput,)):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class NSSGalleryImageForm(forms.ModelForm):
    class Meta:
        model = NSSGalleryImage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput,)) and field_name != 'image':
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class IICPageSettingsForm(forms.ModelForm):
    class Meta:
        model = IICPageSettings
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput,)) and field_name not in ['about_image_1', 'about_image_2']:
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()


class IICGalleryImageForm(forms.ModelForm):
    class Meta:
        model = IICGalleryImage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, (forms.CheckboxInput,)) and field_name != 'image':
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{existing_classes} form-control".strip()



