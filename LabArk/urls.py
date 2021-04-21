from django.contrib import admin
from django.urls import path, re_path

from LabArk import settings
from LabArkApp import views as LA
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    re_path('^admin/?', admin.site.urls),
    re_path(r'^faq', LA.faq, name="faq"),
    re_path(r'^popular', LA.popular, name="popular"),
    re_path(r'^libs', LA.libs, name="libs"),
    re_path(r'^category/(?P<pk>\d+?)', LA.category_labs, name='category_labs'),
    re_path(r'^archive', LA.archive, name="archive"),
    re_path(r'^links', LA.links, name="links"),
    re_path(r'^register', LA.register, name="register"),
    re_path(r'^login', LA.login_view, name="login"),
    re_path(r'^logout', LA.logout_view, name="logout"),
    re_path(r'^details/(?P<pk>\d+)$', LA.details, name="details"),
    re_path(r'^user/(?P<pk>\d+)$', LA.get_profile, name="profile_view"),
    re_path(r'^labs/add$', LA.add_lab, name="lab_add"),
    re_path(r'^category/add/?$', LA.add_category, name="category_add"),
    re_path(r'^random_lab$', LA.get_random_lab, name="random_lab"),
    re_path(r'^inc_downloads$', LA.add_download_to_category, name="inc_download_category"),
    re_path(r'^blog$', LA.blog, name="blog"),
    re_path(r'^add_post$', LA.add_post_to_blog, name="add_post"),
    re_path(r'^premium$', LA.premuim_view, name="premium"),
    re_path(r'^update_rating$', LA.update_rating, name="set_rating"),
    path('', LA.home, name="homepage"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
