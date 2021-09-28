from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')
    # return HttpResponse('Hello, World!')


def register(request):
    if request.user:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("form received")
        if form.is_valid():
            print("the form is valid")
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        messages.error(request, "not valid")
    form = UserCreationForm()
    context = {
        'register_form': form
    }
    return render(request, 'registration/login.html', context)


def logout_request(request):
    logout(request)
    return redirect('login')
