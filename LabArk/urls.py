from django.contrib import admin
from django.urls import path, re_path
from LabArkApp import views as LA

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^faq', LA.faq, name="faq"),
    re_path('', LA.home, name="homepage"),
    re_path('^popular', LA.popular, name="popular"),
    re_path('^libs', LA.libs, name="libs"),
    re_path('^archive', LA.archive, name="archive"),
    re_path('^links', LA.links, name="links"),
]
