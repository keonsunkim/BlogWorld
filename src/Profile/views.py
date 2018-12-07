from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model

from Post.models import GeneralPost

# User_Model = settings.AUTH_USER_MODEL
User_Model = get_user_model()

# Create your views here.


def user_lists(request):
    user_lists = User_Model.objects.all().values()
    user_lists = [user for user in user_lists]
    return HttpResponse(f'<p>{user_lists}</p>')


def user_profile(request, representation_name):
    try:
        profile = User_Model.objects.get(
            representation_name__iexact=representation_name)
        print(request.META)
    except User_Model.DoesNotExist:
        raise Http404("There is no GeneralPost object")
    return HttpResponse(f'<h1>User was found</h1> <br> {profile}')


def user_posts(request, representation_name):
    try:
        user_posts = User_Model.objects.get(
            representation_name__iexact=representation_name
        ).user_posts.all().values()

        user_posts = [post for post in user_posts]
        print(user_posts)
    except User_Model.DoesNotExist:
        raise Http404("There is no GeneralPost object")
    return HttpResponse(f'<p>{user_posts}</p>')
