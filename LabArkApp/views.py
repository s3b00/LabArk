from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from LabArkApp.models import Lab, Category
from . import forms
from random import randint
from django.urls import reverse


def home(request):
    return render(request, 'index.html', context={
        'last_labs': Lab.objects.all(),
        'form': forms.AddCategoryForm()
    })  


def faq(request):
    return render(request, 'faq.html')


def popular(request):
    return render(request, 'popular.html', context={
        'popular_labs': Lab.objects.all().order_by('-views', 'name'),
        'form': forms.AddCategoryForm()
    })


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
        return render(request, 'register.html', context={
            'form': forms.RegisterUser()
        })
    else:
        form = forms.RegisterUser(request.POST)

        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            if request.POST.get("SetLogin") == "1":
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect("/")
                    else:
                        pass

        return HttpResponseRedirect("/")


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def details(request, pk):
    lab = get_object_or_404(Lab, id=pk)
    lab.views += 1
    lab.save()

    return render(request, "lab_view.html", context={
        "lab_object": lab,
    })


def get_profile(request, pk):
    user = get_object_or_404(User, id=pk)
    return render(request, "profile.html", context={
        "user": user
    })


def add_lab(request):
    if request.method == "POST":
        form = forms.UploadLabForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                author = request.user
            else:
                author = User.objects.get_by_natural_key('anonymous')

            lab = Lab(**form.cleaned_data)
            lab.author = author
            lab.category = Category.objects.get(pk=request.POST.get("category"))
            lab.file = request.FILES['file']
            lab.save()

            author.profile.reputation += 10
            author.profile.uploads += 1
            author.save()

            return HttpResponseRedirect(reverse('details', args=[lab.pk]))
        else:
            return HttpResponse(form.errors)
    else:
        return render(request, "add_lab.html", context={
            'form': forms.UploadLabForm(),
            'category': Category.objects.all()
        })


def add_category(request):
    if request.method == "POST":
        category = Category.objects.create(name=request.POST.get("name"))
        category.save()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect('/')


def get_random_lab(request):
    return HttpResponseRedirect(reverse('details', args=[randint(1, Lab.objects.count())]))