from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

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

    form = UserRegisterForm()
    return render(
        request,
        'users/registration.html',
        {
            'title': 'Registration page',
            'form': form
        }
    )
