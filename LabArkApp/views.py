from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return render(request, 'index.html')


def faq(request):
    return render(request, 'faq.html')


def popular(request):
    return render(request, 'popular.html')


def archive(request):
    return render(request, 'archive.html')


def libs(request):
    return render(request, 'libs.html')


def links(request):
    return render(request, 'links.html')


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                pass
        else:
            pass


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return HttpResponseRedirect("/")


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
