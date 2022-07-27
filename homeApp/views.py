from multiprocessing import context
import re
from django.shortcuts import render
from .models import Course, CourseDetails
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def homePage(request):
    courses = Course.objects.all()
    context = {
        "title":"Thrive Tech",
        "courses":courses
    }
    return render(request, "home/index.html", context=context)

def courseView(request, id):
    course = Course.objects.get(id=id)
    courseDetails = CourseDetails.objects.get(course_id = id)
    context = {
        "course":course,
        "courseDetails":courseDetails,
    }
    return render(request, "home/view.html", context=context)


def allCourses(request, courseType):
    if courseType == 'all':
        courses = Course.objects.all()
    elif courseType == 'run':
        courses = Course.objects.filter(running=True)
    elif courseType == 'up':
        courses = Course.objects.filter(running=False)
    context = {
        "title":"Courses",
        "courses":courses
    }
    return render(request, 'home/courses.html', context=context)

# def running_courses(request):
#     run_course = Course.objects.filter(running=True)
#     return render(request, 'home/courses.html')
#     pass 

def about_us(request):
    context = {'title':"About Us"}
    return render(request, 'home/about.html', context=context)


@login_required
def enroll_function(request):
    return HttpResponseRedirect(reverse('homeApp:home-page'))