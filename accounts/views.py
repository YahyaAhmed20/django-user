from urllib import request
from django.shortcuts import redirect, render
from .forms import SignupForm,UserForm,ProfileForm
from django.contrib.auth import authenticate,login
from .models import Profile
from django.urls import reverse


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user and get the user instance
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Check if the user already has a profile
                if not hasattr(user, 'profile'):
                    Profile.objects.create(user=user)  # Create a profile only if it doesn't exist
                return redirect('/accounts/profile')
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profleform = ProfileForm(request.POST, request.FILES, instance=profile)  # Include request.FILES for image uploads
        if userform.is_valid() and profleform.is_valid():
            userform.save()
            profleform.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profleform = ProfileForm(instance=profile)
    
    return render(request, 'accounts/profile_edit.html', {'userform': userform, 'profleform': profleform})