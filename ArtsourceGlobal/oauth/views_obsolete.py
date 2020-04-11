import requests
from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from django.utils.http import urlencode
import json
from subprocess import Popen


def retrieve_authorization_code(client_id, redirect_uri, scope, base_url):
    authorization_code_req = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope
    }

    r = requests.get(base_url + "auth?%s" % urlencode(authorization_code_req),
                     allow_redirects=False)
    url = r.headers.get('location')
    Popen(["open", url])

    authorization_code = input("\nAuthorization Code >>> ")
    return authorization_code


"""
Retrieving access_token and refresh_token from Token API.
"""


def retrieve_tokens(authorization_code, client_id, client_secret, redirect_uri, base_url):
    access_token_req = {
        "code": authorization_code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }
    content_length = len(urlencode(access_token_req))
    access_token_req['content-length'] = str(content_length)

    r = requests.post(base_url + "token", data=access_token_req)
    data = json.loads(r.text)
    return data


def get_userinfo(client_id, redirect_uri, scope, base_url, info_link):
    authorization_code = retrieve_authorization_code(client_id, redirect_uri, scope, base_url)
    tokens = retrieve_tokens(authorization_code, client_id, redirect_uri, scope, base_url)
    access_token = tokens['access_token']
    authorization_header = {"Authorization": "OAuth %s" % access_token}
    r = requests.get(info_link,
                     headers=authorization_header)
    return r.text


def google(request):
    # The below client id and secret should be changed after you get your own id and secret
    client_id = '10025917122-ig33jq7vs6ceg3u48s98orha3n31rg2e.apps.googleusercontent.com'
    client_secret = 'MFSnwDQRxJXq8DaRV3Sv3l3e'
    redirect_uri = 'http:127.0.0.0:8000/oauth/callback'
    authorization_base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    token_url = "https://www.googleapis.com/oauth2/v4/token"
    scope = [
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile"
    ]
    base_url = r"https://accounts.google.com/o/oauth2/"
    info_link = "https://www.googleapis.com/oauth2/v2/userinfo"

    
    message = "nothing received"

    return render(request, "oauth/index.html", {'message': message})


def google_authorization():
    return


def google_callback(request):
    return


def google_token(request):
    return


def google_info(request):
    return
