from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.db import transaction
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages



from .forms import SignUpForm, EditProfileForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            with transaction.atomic():  # Start a transaction
                user = form.save()  # Save the User model created by the form
                user.refresh_from_db()  # Refresh the user instance to get the related objects
                user.userprofile.street_address = form.cleaned_data.get('street_address')
                user.userprofile.city = form.cleaned_data.get('city')
                user.userprofile.state = form.cleaned_data.get('state')
                user.userprofile.zipcode = form.cleaned_data.get('zipcode')
                user.userprofile.phone_number = form.cleaned_data.get('phone_number')
                user.userprofile.save()  # Save the UserProfile model

                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)

                return redirect('/')
        else:
            return render(request, 'userprofile/signup.html', {'form': form})
    else:
        form = SignUpForm() 

    return render(request, 'userprofile/signup.html', {'form': form})

@login_required
def myaccount(request):
    return render(request, 'userprofile/user-account.html')

@login_required
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')

@login_required
def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Set the user field
            user_profile.save()
            return redirect('userprofile:editprofile')
    else:
        form = EditProfileForm(instance=request.user.userprofile)

    return render(request, 'userprofile/edit_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in after changing the password
            messages.success(request, 'Your password was successfully updated!')
            return redirect('userprofile:myaccount')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'userprofile/user-security.html', {
        'form': form
    })
    