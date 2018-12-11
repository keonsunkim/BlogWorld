from django.shortcuts import render

from django.http import HttpResponse, Http404
# Create your views here.


def example_view(request):
    print('request')
    print(request)
    print('*' * 20)
    print('request.method')
    print(request.method)
    print('*' * 20)
    print('request.body')
    print(request.body)
    print('*' * 20)
    print('request.path')
    print(request.path)
    print('*' * 20)
    print('request.cookies')
    print(request.COOKIES)
    print('*' * 20)
    print('request.meta')
    print(request.META)
    return HttpResponse(f'<h1> Hi!!! </h1>')
