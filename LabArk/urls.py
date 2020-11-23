from django.contrib import admin
from django.urls import path, re_path
from LabArkApp import views as LA

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', LA.home, name="homepage"),
    re_path(r'^faq', LA.faq, name="faq")
]