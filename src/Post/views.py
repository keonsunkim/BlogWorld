from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import GeneralPost
# Create your views here.


def detail(request, post_id):
    try:
        post = GeneralPost.objects.get(pk=post_id)
        print(request)
        print(post_id)
    except GeneralPost.DoesNotExist:
        raise Http404("There is no GeneralPost object")
    return HttpResponse(f'<h1>Page was found</h1> <br> {post}')


def post_list(request):
    posts = GeneralPost.objects.all()
    return HttpResponse(f'{posts}')
