from django.contrib import admin
from django.urls import path, re_path
from LabArkApp import views as LA

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^faq', LA.faq, name="faq"),
    re_path(r'^popular', LA.popular, name="popular"),
    re_path(r'^libs', LA.libs, name="libs"),
    re_path(r'^archive', LA.archive, name="archive"),
    re_path(r'^links', LA.links, name="links"),
    re_path(r'^register', LA.register, name="register"),
    re_path(r'^login', LA.login_view, name="login"),
    re_path(r'^logout', LA.logout_view, name="logout"),
    re_path(r'^details/(?P<id>\d+?)', LA.details, name="details"),
    re_path('', LA.home, name="homepage"),
]
