from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.views import View

from user import models
from .email_send import send_code_email
from .form import UserForm, RegisterForm
import hashlib

from .models import EmailVerifyRecord

artist_choices = {
    'Yes': True,
    'No': False,
}


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                # search user by email
                active_user = models.User.objects.get(email=email)
                # activate user
                active_user.is_active = True
                active_user.save()
                record.delete()  # the record not longer needed
                request.session['is_login'] = True
                request.session['user_id'] = active_user.id
                request.session['user_name'] = active_user.username
                return redirect('/user/index/')
        else:
            # probably need resend
            return render(request, "verification_fail.html")


def login(request):
    if request.session.get('is_login', None):  # reject login if already logged in
        return redirect('/user/index')

    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = 'Please check the provided information'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(username=username)
                if not user.is_active:
                    message = 'Please verify email first'
                    return render(request, 'user/login.html', locals())
                # match the hashcode
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/user/index/')
                else:
                    message = 'password is incorrect'
            except Exception as e:
                print(e)
                message = 'username is not exist'
        return render(request, 'user/login.html', locals())
    login_form = UserForm()
    # return render(request, 'user/login.html')
    return render(request, 'user/login.html', locals())


def index(request):
    pass
    return render(request, 'user/index.html')


def register(request):
    if request.session.get('is_login', None):
        # cant register when logged in
        return redirect('/user/index/')

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        # Get the form
        # check_box_list = request.POST.getlist('check_box_list')
        # for i in check_box_list:
        #     print(check_box_list)
        #     if i == '1':
        #         print("the form returns integer")
        #     print("the term function")  # i.e. add the term choice to db
        message = 'Please check the provided information'
        check_term = request.POST.get('term_check')  # another method to get check box, or can use form.cleaned_data

        if check_term == 'on':
            if register_form.is_valid():
                # dont wanna fill form again
                # username = register_form.cleaned_data['username']

                stored_form = register_form
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
                    same_name_user = models.User.objects.filter(username=username)
                    # check user name
                    if same_name_user:
                        message = 'The user name was already existed'
                        return render(request, 'user/register.html',
                                      {'message': message, 'register_form': stored_form})

                    same_email_user = models.User.objects.filter(email=email)
                    if same_email_user:
                        message = 'The email was registered, please use another one'
                        return render(request, 'user/register.html',
                                      {'message': message, 'register_form': stored_form})

                    artist = request.POST.get('artist')
                    if artist == 'on':
                        ref_email = request.POST.get('refEmail')
                        if models.User.objects.filter(email=ref_email):
                            message = 'Sorry, cant find your referee\'s email'
                            return render(request, 'user/register.html',
                                          {'message': message, 'register_form': stored_form})

                    # create the user
                    new_user = models.User()
                    new_user.username = username
                    # use encrypted password
                    new_user.password = hash_code(password1)
                    new_user.email = email
                    # record additional info
                    additional_info = request.POST.get('additionalInfo')
                    street1 = request.POST.get('street1')
                    new_user.additionalInfo = models.AdditionalInfo()
                    if additional_info == 'on' or street1 != '':  # they may fill the form and close the tab
                        new_user.additionalInfo.gender = request.POST.get('gender')
                        new_user.additionalInfo.age = int(request.POST.get('age'))
                        new_user.additionalInfo.street1 = street1
                        new_user.additionalInfo.street2 = request.POST.get('street2')
                        new_user.additionalInfo.suburb = request.POST.get('suburb')
                        new_user.additionalInfo.state = request.POST.get('state')
                        new_user.additionalInfo.postalCode = request.POST.get('postalCode')
                        new_user.additionalInfo.country = request.POST.get('country')
                        new_user.additionalInfo.phone = request.POST.get('phone')

                    # record interest
                    new_user.interest = models.Interest()
                    if request.POST.get('painting') == 'on':
                        new_user.interest.painting = True
                    if request.POST.get('sculpture') == 'on':
                        new_user.interest.sculpture = True
                    if request.POST.get('photography') == 'on':
                        new_user.interest.photography = True
                    if request.POST.get('calligraphy') == 'on':
                        new_user.interest.calligraphy = True
                    if request.POST.get('printmaking') == 'on':
                        new_user.interest.printmaking = True
                    if request.POST.get('artsAndCrafts') == 'on':
                        new_user.interest.artsAndCrafts = True
                    if request.POST.get('sealCutting') == 'on':
                        new_user.interest.sealCutting = True
                    if request.POST.get('artDesign') == 'on':
                        new_user.interest.artDesign = True
                    new_user.is_active = False
                    if artist == 'on':
                        new_user.artist = True
                        ref_email = request.POST.get('refEmail')
                        new_user.refEmail = ref_email
                        real_name = request.POST.get('realName')
                        send_code_email(email, referee_email=ref_email, send_type="register",
                                        real_name=real_name, is_artist=True)
                    else:
                        send_code_email(email, send_type="register")
                        new_user.save()
                        new_user.additionalInfo.save()
                        new_user.interest.save()
                    return redirect('/user/login/')
    # if request is not valid, return a RegisterForm
    register_form = RegisterForm()

    # render a form with error message
    return render(request, 'user/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # no login, no logout
        return redirect('/user/index/')
    request.session.flush()
    # or we can use the code below, should has the same effect if dont add new session keys
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect('/user/index/')


# The hash function used to encrypt password
def hash_code(s, salt='artsource'):
    h = hashlib.sha256()
    s += salt
    # update only accept bytes
    h.update(s.encode())
    return h.hexdigest()
