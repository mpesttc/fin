from crypt import methods

from IPython.core.pylabtools import retina_figure
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from my_finances.forms import LoginForm


def home(request):
    return HttpResponse("My Finances home page")

def register_view(request):
    print(f'Got {request.method} method')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('Form validation...')
        if form.is_valid():
            print('The form is valid')
            print(form.cleaned_data)
            form.save()
            return redirect("/finance/login")
    else:
        form = UserCreationForm()
    return render(request, "my_finances/register.html", {"form":form})

def user_login(request):
    if request.method == 'POST':
        print(f'POST: {request.POST}')
        form = LoginForm(data=request.POST)
        print('Form validation...')
        if form.is_valid():
            print('The form is valid')
            cd = form.cleaned_data
            print(cd)
            user = authenticate(username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return redirect("/finance/")
            else:
                return HttpResponse("User not found")
        else:
            return HttpResponse("Invalid login")
    else:
        print(f'Jast new form: {request.GET}')
        form = LoginForm()

    return render(request, "my_finances/login.html", {"form":form})
