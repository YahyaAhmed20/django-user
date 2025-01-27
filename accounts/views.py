from django.shortcuts import redirect, render
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from .models import Profile

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