from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def faq(request):
    return render(request, 'faq.html')
