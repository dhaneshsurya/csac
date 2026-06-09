from django.shortcuts import render, get_object_or_404
from .models import Department, Program, COPOMapping, AcademicCalendar, Syllabus


def department_detail(request, slug):
    dept = get_object_or_404(Department, slug=slug)
    faculty = dept.faculty.all()
    activities = dept.activities.all()[:6]
    programs = dept.programs.all()
    copo = dept.copo_mappings.all()
    syllabi = dept.syllabi.all()
    happenings = dept.happenings.all()
    context = {
        'dept': dept,
        'faculty': faculty,
        'activities': activities,
        'programs': programs,
        'copo': copo,
        'syllabi': syllabi,
        'happenings': happenings,
        'page_title': dept.name,
        'breadcrumb': f"Department of {dept.name}",
    }
    return render(request, 'academics/department_detail.html', context)


def programs(request):
    all_programs = Program.objects.select_related('department').all()
    ug_programs = all_programs.filter(program_type='ug')
    pg_programs = all_programs.filter(program_type='pg')
    diploma_programs = all_programs.filter(program_type='diploma')
    departments = Department.objects.all()
    context = {
        'all_programs': all_programs,
        'ug_programs': ug_programs,
        'pg_programs': pg_programs,
        'diploma_programs': diploma_programs,
        'departments': departments,
        'page_title': 'Programs Offered',
        'breadcrumb': 'Programs Offered',
    }
    return render(request, 'academics/programs.html', context)


def academic_calendar(request):
    calendars = AcademicCalendar.objects.filter(is_active=True)
    context = {
        'calendars': calendars,
        'page_title': 'Academic Calendar',
        'breadcrumb': 'Academic Calendar',
    }
    return render(request, 'academics/academic_calendar.html', context)
