from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
from django.urls import reverse


@login_required
def home(request):
    user_profile = request.user.XP_points
    return render(request, 'home.html', context={
        'user_profile': user_profile
    })
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
        'register_form': form,
        'form': AuthenticationForm()
    }
    return render(request, 'registration/login.html', context)


def logout_request(request):
    logout(request)
    return redirect('login')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('home'))
        else:
            messages.error(request, 'username or password not correct')
            return redirect(reverse('login'))


    else:
        form = AuthenticationForm()
        register_form = UserCreationForm()
    return render(request, 'registration/login.html', {'form': form, 'register_form': register_form})
