from django.conf.urls import include, url

from . import views

urlpatterns = [
    url
    url(r'^(?P<post_id>[0-9]+)/$', views.detail),
]
