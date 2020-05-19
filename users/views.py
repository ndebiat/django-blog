from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    # put a check in place, only validate a form if you get a POST request (else stays blank)
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)

        # check that all form data submitted is valid
        # validation automatically in django's form feature, passed in and created by the form = UserCreationForm above
        if form.is_valid():
            # save the form to the database
            # django automatically hashes the password and everything
            form.save()

            # show message alerting user of success
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            # redirect the user to the home page
            return redirect('login')
    else:
        form = UserRegisterFrom()  # otherwise, a form is made that stays blank

    return render(request, 'users/register.html', {'form': form})


# require a user to be logged in to view
# need to change route of the log_required to the login page, done in settings.py file
# after the login is done, django has parameters in place to allow you to redirect to profile
@login_required()
def profile(request):
    # when the user update, have the fields filled in with current username and email
    # using instance=request.
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # save profile information if valid
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            # success message and redirect
            messages.success(request, f'Account updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
