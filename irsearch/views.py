from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


def index(request):
    return render(request,'pages/base.html')

def index_result(request):
    return render(request, 'pages/result.html')
