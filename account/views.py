from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib import messages

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin



def register_account(request):
    if request.method == 'GET':
        return render(request, 'account/register_account.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:

                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('account:profileuser')
            except IntegrityError:
                return render(request, 'account/register_account.html',
                              {'form': UserCreationForm(), 'error': 'User already exists'})
        else:
            return render(request, 'account/register_account.html',
                          {'form': UserCreationForm(), 'error': 'Passwords do not match'})



def login_account(request):
    if request.method == 'GET':
        return render(request, 'account/login.html', {'form': AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'account/login.html',
                          {'form': AuthenticationForm(),
                           'error': 'User or password not defined. Register'})
        else:
            login(request, user)
            return redirect('account:profileuser')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homeapp:homepage')


 
@login_required
def profileuser(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('account:profileuser')
        else:
            return render(request, 'account/profileuser.html', {'profile_form': profile_form})    
    else:
        profile_form = ProfileForm()
        return render(request, 'account/profileuser.html', {'profile_form': profile_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('account:profileuser')        