from django.shortcuts import render
from passwordpractice.forms import UserProfileInfoForm,UserForm

# for login and logout for the website
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	# print(request.headers)
	# print(request.META['HTTP_USER_AGENT'])
	return render(request,'passwordpractice/index.html')
# @login_required is a decorators

@login_required
def special(request):
        return HttpResponse("You are logged in, Nice!") 

@login_required
def user_logout(request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

def register(request):

        registered = False
        if request.method == "POST":
                user_form = UserForm(data=request.POST) 
                profile_form = UserProfileInfoForm(data=request.POST)

                if user_form.is_valid() and profile_form.is_valid():
                        user = user_form.save()
                        user.set_password(user.password)
                        user.save()

                        profile = profile_form.save(commit=False)
                        profile.user = user

                        # to check if the user has actually uploaded the profile pic or not
                        if 'profile_pic' in request.FILES:
                                profile.profile_pic = request.FILES['profile_pic']

                        profile.save()

                        registered = True
                else:
                        print(user_form.errors,profile_form.errors)
        else:
                user_form = UserForm()
                profile_form = UserProfileInfoForm()
        return render(request,'passwordpractice/registration.html',
        {'user_form':user_form,
         'profile_form':profile_form,
         'registered':registered})


# the 'username' above in quotes should be same as name 'username' in input field in login.html file.
def user_login(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                
                user = authenticate(username=username,password=password)   

                if user:
                        if user.is_active:
                                login(request,user)
                                return HttpResponseRedirect(reverse('index'))

                        else:
                                return HttpResponse("ACCOUNT NOT ACTIVE")
                else:
                        print("Someone tried to login and failed!")
                        print("Username:{} and password:{}".format(username,password))
                        return HttpResponse("invalid login details supplied!")
        else:
                return render(request,'passwordpractice/login.html',{})
                        




         