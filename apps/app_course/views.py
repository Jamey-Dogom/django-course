from django.shortcuts import render, redirect
from apps.app_course.models import *

def index(request):
    all_courses = Course.objects.all()
    context = {
        "all_courses": all_courses
    }

    return render(request, "app_course/index.html", context)

def delete(request, course_id):
    delete_course = Course.objects.get(id = course_id)
    context = {
        "delete_course": delete_course
    }
    return render(request, "app_course/delete.html", context)

def destroy(request, course_id):
    destroy_course = Course.objects.get(id = course_id)
    destroy_course.delete()
    return redirect('/')

def add(request):
    new_course = Course.objects.create(name = request.POST['course_name'])

    Description.objects.create(course = new_course, desc = request.POST['course_desc'])
    return redirect('/')