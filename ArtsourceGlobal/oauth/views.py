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
