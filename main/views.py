from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from .models import *
import random
from django.urls import reverse
# Create your views here.



def index(request):
    return render(request , 'main/index.html')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password_confirm = request.POST["confirm-password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        if password == password_confirm:
            user = User.objects.create_user(username, email, password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            a_user = User.objects.get(username=username)
            a = Student(id=None, s_user=a_user)
            a.save()
            # if reg_id == 1:
            #     s_user = Author.objects.create(t_user=User.objects.get(user.id))
            #     s_user.save()
            # else:
            #     s_user = Student.objects.create(t_user=User.objects.get(user.id))
            #     s_user.save()
            # login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'main/register.html', {
                "message": "passwords do not match"
            })

    return render(request, 'main/register.html')

def t_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password_confirm = request.POST["confirm-password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        if password == password_confirm:
            user = User.objects.create_user(username, email, password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            b_user = User.objects.get(username=username)
            b = Author(id=None, t_user=b_user)
            b.save()
            # if b.is_valid:
            #     b.save()
            # else:
            #     print("smth")
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'main/t_register.html', {
                "message": "passwords do not match"
            })

    return render(request, 'main/t_register.html')


def login_view(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request , username=username , password=password)
        if user is not None and user:
            login(request , user)
            return HttpResponseRedirect(reverse('std_dash'))
        else:
            return render(request , 'main/log_in.html',{
                "message": "Invalid login or password"
            })

    return render(request ,'main/log_in.html')

def logout_view(request):
    logout(request)
    return render(request , 'main/log_in.html' , {
        "message":"You logged out"
    })

def courses(request):
    programs = Program.objects.all()
    return render(request, 'main/programs.html', {
        "programs":programs
    })

def notifications(request):
    if request.user.is_superuser:
        authors = Author.objects.filter(is_active=False, is_declined=False)
        return render(request , 'main/admin_panel.html', {
            "authors": authors
        })
    return render(request, 'main/log_in.html', {
        "message": "please login as an admin"
    })

def confirm_author(request, con_id):
    if request.user.is_superuser:
        selected_auth = Author.objects.get(t_user=User.objects.get(pk=con_id))
        selected_auth.is_active = True
        selected_auth.save()
        return HttpResponseRedirect(reverse('notifications'))
    elif Exception:
        return render(request, 'main/admin_panel.html')
    else:
        return render(request, 'main/log_in.html', {
        "message": "please login as an admin"
    })



def decline_author(request, con_id):
    if request.user.is_superuser:
        selected_auth = Author.objects.get(t_user=User.objects.get(pk=con_id))
        selected_auth.is_declined = True
        selected_auth.save()
        return HttpResponseRedirect(reverse('notifications'))
    elif Exception:
        return render(request, 'main/admin_panel.html')

def std_by_num(request):
    if request.user.is_superuser:
        programs = Program.objects.all()
        return render(request , 'main/std_by_num.html',{
            "programs": programs
        })
    return render(request, 'main/log_in.html', {
        "message": "please login as an admin"
    })

def std_dash(request):
    user = User.objects.get(pk=request.user.id)
    student = Student.objects.get(s_user=user)
    return render(request, 'main/std_dash.html',{
        "user":user,
        "student": student
    })

def profile(request):
    user = User.objects.get(pk= request.user.id) 
    return render(request , 'main/profile.html' ,{
        'user':user
    })

def detail(request , program_id):
    program = Program.objects.get(pk = program_id)

    return render(request, 'main/program_detail.html', {
        "program": program
    })