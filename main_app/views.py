from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'welcome.html')
    # return HttpResponse('Hello, World!')


class Login():
    pass
