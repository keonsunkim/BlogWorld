from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import GeneralPost
# Create your views here.


def post_list(request):
    posts = GeneralPost.objects.all().values()
    posts = [post for post in posts]
    print(posts)
    return HttpResponse(f'<p>{posts}</p>')


def post_detail(request, post_id):
    try:
        post = GeneralPost.objects.get(pk=post_id)
        print(request.META)
        print(post_id)
    except GeneralPost.DoesNotExist:
        raise Http404("There is no GeneralPost object")
    return HttpResponse(f'<h1>Page was found</h1> <br> {post}')
