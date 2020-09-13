from django.shortcuts import render, redirect
from django.contrib import messages # debug, info, success, warning etc.
from .forms import UserRegisterForm

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
            messages.success(request, f"Account created for {username}!")
            # redirect back user to home page
            return redirect('blog-home')

    else: 
        form = UserRegisterForm() # creating a blank form
    return render (request, 'users/register.html', {'form': form})

