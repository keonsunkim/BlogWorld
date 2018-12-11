from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^(?P<representation_name>[\w]+)/$', views.user_profile),
    url(r'^(?P<representation_name>[\w]+)/post/$', views.user_posts),
    url(r'', views.user_lists),
]
