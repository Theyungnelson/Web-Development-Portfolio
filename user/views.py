from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
#! create a new user account
def userRegister(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogHome')
    else:
        form = UserCreationForm()  
    return render(request, "user/register.html", {"form" : form})

#! allow user to login to there account
def userLogin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, user=form.get_user())
            return redirect('blogHome')
    else:
        form = AuthenticationForm() 
    return render(request, "user/login.html", {"form" : form})

    

#! user logout from the accout
def userLogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('userlogin')
