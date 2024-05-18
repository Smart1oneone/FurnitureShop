from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context = {
        'title': 'home',
        'content': 'yo1',
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('about')