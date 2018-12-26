from django.shortcuts import render

from django.http import HttpResponse, Http404
# Create your views here.


def homepage_view(request):
    context = {}
    return render(request, "home/ourpage.html", context)


def example_view(request):
    if request.COOKIES:
        return HttpResponse(f'<h1> Hi!!! </h1>')
    else:
        raise Http404('you do not have cookies go away')
