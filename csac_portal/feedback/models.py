from django.db import models


class StudentFeedback(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    student_name = models.CharField(max_length=150)
    roll_number = models.CharField(max_length=30, blank=True)
    program = models.CharField(max_length=200)
    year_of_study = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=10)
    teaching_quality = models.IntegerField(choices=RATING_CHOICES)
    infrastructure = models.IntegerField(choices=RATING_CHOICES)
    library_resources = models.IntegerField(choices=RATING_CHOICES)
    sports_facilities = models.IntegerField(choices=RATING_CHOICES)
    overall_experience = models.IntegerField(choices=RATING_CHOICES)
    suggestions = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Student Feedback"
        verbose_name_plural = "Student Feedback"

    def __str__(self):
        return f"{self.student_name} ({self.academic_year})"


class ParentFeedback(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    parent_name = models.CharField(max_length=150)
    student_name = models.CharField(max_length=150)
    program = models.CharField(max_length=200)
    academic_year = models.CharField(max_length=10)
    teaching_quality = models.IntegerField(choices=RATING_CHOICES)
    communication = models.IntegerField(choices=RATING_CHOICES)
    safety = models.IntegerField(choices=RATING_CHOICES)
    overall_satisfaction = models.IntegerField(choices=RATING_CHOICES)
    suggestions = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Parent Feedback"
        verbose_name_plural = "Parent Feedback"

    def __str__(self):
        return f"{self.parent_name} - Parent of {self.student_name}"


class FacultyFeedback(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    faculty_name = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    academic_year = models.CharField(max_length=10)
    infrastructure = models.IntegerField(choices=RATING_CHOICES)
    admin_support = models.IntegerField(choices=RATING_CHOICES)
    research_support = models.IntegerField(choices=RATING_CHOICES)
    work_environment = models.IntegerField(choices=RATING_CHOICES)
    overall_satisfaction = models.IntegerField(choices=RATING_CHOICES)
    suggestions = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Faculty Feedback"
        verbose_name_plural = "Faculty Feedback"

    def __str__(self):
        return f"{self.faculty_name} ({self.department})"


class AlumniFeedback(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    alumni_name = models.CharField(max_length=150)
    batch_year = models.IntegerField()
    program = models.CharField(max_length=200)
    current_status = models.CharField(max_length=200, blank=True, help_text="e.g. Employed at XYZ / Higher Studies")
    teaching_quality = models.IntegerField(choices=RATING_CHOICES)
    campus_experience = models.IntegerField(choices=RATING_CHOICES)
    career_support = models.IntegerField(choices=RATING_CHOICES)
    overall_experience = models.IntegerField(choices=RATING_CHOICES)
    suggestions = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = "Alumni Feedback"
        verbose_name_plural = "Alumni Feedback"

    def __str__(self):
        return f"{self.alumni_name} (Batch {self.batch_year})"
