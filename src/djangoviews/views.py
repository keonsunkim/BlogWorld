from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.conf import settings

from Post.models import GeneralPost
from django.contrib.auth import get_user_model

User = get_user_model()
# User = settings.AUTH_USER_MODEL

# Create your views here.


def homepage_view(request):
    context = {}
    all_post = GeneralPost.objects.all()
    context['all_posts'] = all_post

    return render(request, "home/ourpage.html", context)


def example_view(request):
    if request.COOKIES:
        return HttpResponse(f'<h1> Hi!!! </h1>')
    else:
        raise Http404('you do not have cookies go away')
