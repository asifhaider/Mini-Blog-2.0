from django.shortcuts import render, redirect
from django.contrib import messages # debug, info, success, warning etc.
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# import login decorator 
from django.contrib.auth.decorators import login_required


# replacing inherited registration from with the older one

# classes that will convert into django html forms

def register (request):
    # adding condition for get and post http requests

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # adding validations
        if form.is_valid():
            form.save()

            username= form.cleaned_data.get('username')
            # show a flash message
            messages.success(request, f"Account created for {username}! You can Login now!")
            # redirect back user to home page
            return redirect('blog-home')

    else: 
        form = UserRegisterForm() # creating a blank form
    return render (request, 'users/register.html', {'form': form})

@login_required
def profile (request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                request.FILES, 
                                instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Account has been updated!")
            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

