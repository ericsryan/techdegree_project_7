from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . import forms


def index(request):
    """Display site home page."""
    return render(request, 'index.html')


# def user_profile_view(request):
#     form = forms.UserProfileForm()
#     if request.method == 'POST':
#         form = forms.UserProfileForm(request.POST)
#         if form.is_valid():
#             messages.add_message(request, messages.SUCCESS, "Form submitted")
#             return HttpResponseRedirect(reverse('user_profile'))
#     return render (request, 'user_profile_form.html', {'form': form})


def sign_up(request):
    form = forms.RegisteredUserForm()

    if request.method == 'POST':
        form = forms.RegisteredUserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "You have been successfully registered!")
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'sign_up_form.html', {'form': form})
