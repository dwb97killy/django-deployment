from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from first_app.models import AccessRecord, Topic, Web
from . import forms
from first_app.forms import NewUser, UserForm, User_info
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    # return HttpResponse("<em>Hello World!</em>")  # Each view must return as a HttpResponse object
    return render(request, 'index.html')

def index_1(request):
    web_list = AccessRecord.objects.order_by('date')
    my_dict = {"input": "This is the input!", "num": 100, 'access_records': web_list}
    return render(request, 'index1.html', context=my_dict)

def form_view(request):
    form = forms.FormName
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        print(form)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print(form.cleaned_data)
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'form_page.html', {'form': form})


def user_view(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'users.html', {'form': form})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_info = User_info(data=request.POST)
        if user_form.is_valid() and profile_info.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_info.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors, profile_info.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = User_info()

        # This is the render and context dictionary to feed
        # back to the registration.html file page.
    return render(request, 'registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            # Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        # Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html', {})


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))