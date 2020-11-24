from django.shortcuts import render


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
