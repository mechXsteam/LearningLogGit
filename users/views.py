from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

"""New users must register first"""

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # log in the user and then redirect to home page
            login(request,new_user)
            return redirect('learning_log:index')
    # Display a blank invalid form
    context = {'form':form}
    return render(request,'registration/register.html',context)

