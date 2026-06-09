from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentFeedbackForm, ParentFeedbackForm, FacultyFeedbackForm, AlumniFeedbackForm


def student_feedback(request):
    if request.method == 'POST':
        form = StudentFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your valuable feedback!')
            return redirect('feedback:student_feedback')
    else:
        form = StudentFeedbackForm()
    return render(request, 'feedback/student_feedback.html', {
        'form': form, 'page_title': "Student's Feedback", 'breadcrumb': "Student's Feedback Form"
    })


def parent_feedback(request):
    if request.method == 'POST':
        form = ParentFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your valuable feedback!')
            return redirect('feedback:parent_feedback')
    else:
        form = ParentFeedbackForm()
    return render(request, 'feedback/parent_feedback.html', {
        'form': form, 'page_title': "Parent's Feedback", 'breadcrumb': "Parent's Feedback Form"
    })


def faculty_feedback(request):
    if request.method == 'POST':
        form = FacultyFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your valuable feedback!')
            return redirect('feedback:faculty_feedback')
    else:
        form = FacultyFeedbackForm()
    return render(request, 'feedback/faculty_feedback.html', {
        'form': form, 'page_title': "Faculty's Feedback", 'breadcrumb': "Faculty's Feedback Form"
    })


def alumni_feedback(request):
    if request.method == 'POST':
        form = AlumniFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your valuable feedback!')
            return redirect('feedback:alumni_feedback')
    else:
        form = AlumniFeedbackForm()
    return render(request, 'feedback/alumni_feedback.html', {
        'form': form, 'page_title': "Alumni's Feedback", 'breadcrumb': "Alumni's Feedback Form"
    })
