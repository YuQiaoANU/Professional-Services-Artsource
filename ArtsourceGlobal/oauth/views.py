import requests
from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.utils.http import urlencode
import json
# from authlib.integrations.httpx_client import AsyncOAuth2Client
from authlib.integrations.requests_client import OAuth2Session
from asg_web_app import settings
from asg_web_app.settings import oauth
from user.models import User, AdditionalInfo, Interest
from user.form import RegisterForm


# TODO: set up the https to test
def google(request):
    # The below client id and secret should be changed after you get your own id and secret
    redirect_uri = 'https://localhost:8000/oauth/google_callback'
    google = oauth.create_client('google')
    return google.authorize_redirect(request, redirect_uri)


def google_callback(request):
    print("in the callback")
    # google = oauth.create_client('google')
    token = oauth.google.authorize_access_token(request)
    user = oauth.google.userinfo(request)
    # do something with the token and profile
    message = "nothing received"
    print(request.get_full_path())
    print("hi")
    print(token)
    print(user)
    return render(request, "oauth/index.html", {'message': message})


def facebook(request):
    # The below client id and secret should be changed after you get your own id and secret
    redirect_uri = 'https://localhost:8000/oauth/facebook_callback'
    facebook = oauth.create_client('facebook')
    return facebook.authorize_redirect(request, redirect_uri)


def facebook_callback(request):
    print("in the facebook callback")
    # facebook = oauth.create_client('facebook')
    token = oauth.facebook.authorize_access_token(request)
    user = oauth.facebook.userinfo(request)
    # do something with the token and profile
    message = "nothing received"
    print(request.get_full_path())
    print("hi")
    print(token)
    print(user)
    return render(request, "oauth/index.html", {'message': message})


def github(request):
    # The below client id and secret should be changed after you get your own id and secret
    redirect_uri = 'https://localhost:8000/oauth/github_callback'
    github = oauth.create_client('github')
    return github.authorize_redirect(request, redirect_uri)


def github_callback(request):
    token = oauth.github.authorize_access_token(request)
    resp = oauth.github.get(url='https://api.github.com/user', token=token)
    profile = resp.json()
    # do something with the token and profile
    return github_redirect(request, profile)


def github_redirect(request, profile):
    message = 'please register your account here!'
    new_user_name = profile['login']
    same_user_name = User.objects.filter(username=new_user_name)
    if same_user_name:
        message += 'The user name was already existed, please choose a new one'
        new_user_name = ''
    email = profile['email']
    if email is None:
        email = ''
    register_form = RegisterForm(initial={
        'username': new_user_name,
        'email': email,
    })
    return render(request, "oauth/oauth_register.html", {'message': message, 'register_form': register_form})


def final_register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        check_term = request.POST.get('term_check')  # another method to get check box, or can use form.cleaned_data
        if check_term == 'on':
            stored_form = register_form
            if register_form.is_valid():
                # dont wanna fill form again
                # username = register_form.cleaned_data['username']
                register_form.clean()
                username = request.POST.get('username')
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                email = request.POST.get('email')
                # check passwords are the same
                if password1 != password2:
                    message = 'Not the same password'
                    return render(request, 'user/register.html', {'message': message, 'register_form': stored_form})
                else:
                    same_name_user = User.objects.filter(username=username)
                    # check user name
                    if same_name_user:
                        message = 'The user name was already existed'
                        return render(request, 'user/register.html',
                                      {'message': message, 'register_form': stored_form})

                    same_email_user = User.objects.filter(email=email)
                    if same_email_user:
                        message = 'The email was registered, please use another one'
                        return render(request, 'user/register.html',
                                      {'message': message, 'register_form': stored_form})
                interest = Interest()
                user = User()
                additional_info = AdditionalInfo()
                additional_info.save()
                interest.save()
                user.additionalInfo = additional_info
                user.interest = interest
                user.email = email
                user.password = password1
                user.username = username
                user.is_active = True
                user.save()
                # TODO: label as todo to ensure later check
                # the user was logged without verification of their email, may need change here
                request.session['is_login'] = True
                request.session['user_name'] = user.username
                return redirect('/user/index/')

    register_form = RegisterForm()
    message = 'There are something with the submitted form'

    return render(request, "oauth/oauth_register.html", locals())
