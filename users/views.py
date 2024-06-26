from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} was successfully registered!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {
            'title': 'Registration page',
            'form': form
        }
    )


@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        if profileForm.is_valid() and updateUserForm.is_valid():
            updateUserForm.save()
            profileForm.save()
            messages.success(request, f'Data updated successfully!')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm
    }
    return render(request, 'users/profile.html', data)
