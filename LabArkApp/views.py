from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  

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
    return render(request, 'index.html', context={
        'last_labs': Lab.objects.all().order_by('-views', 'name'),
        'form': forms.AddCategoryForm(),
        'message': "Самые просматриваемые записи на платформе Labark"
    })

    
def category_labs(request, pk):
    return render(request, 'index.html', context={
        'last_labs': Lab.objects.all().filter(category__pk=pk),
        'form': forms.AddCategoryForm(),
        'message': "Все записи, имеющие категорию " + get_object_or_404(Category, pk=pk).name
    })


def archive(request):
    name = request.GET.get('name', "")
    variant = request.GET.get('variant', "")
    year = request.GET.get('year', '')
    category = request.GET.get('category', '0')

    last_data = {'name': name, 
    'variant': variant, 
    'year':year, 
    'category':category
    }

    return render(request, 'archive.html', context={
        'last_labs': Lab.objects.filter(name__icontains=name, variant__icontains=variant, year__icontains=year, category__pk=category) if int(category) > 0 
        else Lab.objects.filter(name__icontains=name, variant__icontains=variant, year__icontains=year),
        'form': forms.AddCategoryForm(),
        'message': "Не можете определится в том, что ищете? Используйте гибкие фильтры! :)",
        'category': Category.objects.all(),
        'last_data': last_data
    })


def libs(request):
    return render(request, 'libs.html', context={
        'categories': Category.objects.all()
    })


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
            return HttpResponseRedirect(reverse('login'))


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
                user = authenticate(username=user.username, password=form.cleaned_data['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect("/")
            return HttpResponseRedirect("/")
        else:
            return render(request, 'register.html', context={
                'form': forms.RegisterUser(),
                'errors': form.errors
            })


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
    last_labs = Lab.objects.all().filter(author__pk=pk)
    paginator = Paginator(last_labs, 10)  

    page = request.GET.get('page_number') 

    try:  
        labs_object = paginator.get_page(page)  
    except PageNotAnInteger:  
        labs_object = paginator.get_page(1)  
    except EmptyPage:  
        labs_object = paginator.get_page(paginator.num_pages) 

    return render(request, "profile.html", context={
        'user': user,
        'last_labs': labs_object,
        'page': page
    })


def add_lab(request):
    if request.method == "POST":
        form = forms.UploadLabForm(request.POST)

        isFileNotUploaded = False
        try:
            print(request.FILES['file'])
        except:
            isFileNotUploaded = True

        if form.is_valid() and not isFileNotUploaded:
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
            return render(request, 'add_lab.html', context={
                'form': forms.UploadLabForm(),
                'category': Category.objects.all(),
                'errors': form.errors,
                'file_not_uploaded': isFileNotUploaded
            })
    else:
        return render(request, "add_lab.html", context={
            'form': forms.UploadLabForm(),
            'category': Category.objects.all()
        })


def add_category(request):
    if request.method == "POST":
        form = forms.AddCategoryForm(request.POST)
        
        if form.is_valid():
            category = Category.objects.create(name=form.cleaned_data['name'])
            category.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def get_random_lab(request):
    return HttpResponseRedirect(reverse('details', args=[randint(1, Lab.objects.count())]))


def add_download_to_category(request):
    if request.method == "GET":
        category_object = get_object_or_404(Category, pk=request.GET.get('category'))
        category_object.downloads += 1
        category_object.save()
        lab_object = get_object_or_404(Lab, pk=request.GET.get('lab'))
        lab_object.downloads += 1
        lab_object.save()
        return HttpResponseRedirect(reverse('details', args=[lab_object.id]))
