from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
from .models import Applications
import random

def user_info(request):
    from django.contrib.auth.models import User
    if request.user.is_authenticated:
        username=request.user.username
        return {'person':username}
    return {}

def HOME(request):
    if request.method=="POST":
        name=request.POST.get("name")
        c_number=request.POST.get("contact-number")
        email=request.POST.get("email")
        dob=request.POST.get("dob")
        cv=request.POST.get("cv")
        applications=Applications(NAME=name, CONTACT_NUMBER=c_number, EMAIL=email, DOB=dob, CV=cv)
        applications.save()
        name,c_number,email,dob,cv="","","","",""
        messages.success(request, "Your application hass been submited successfull, HR will contact you within 2-3 days.")
        return redirect("/")

    return render(request, 'HOME.html', user_info(request))

# def CONTENT(request):
#     if request.user.is_anonymous:
#         return redirect('/signin/')
#     return render(request, 'CONTENT.html')

def SIGNIN(request):
    # if request.method=="POST":
    #     f_name=request.POST.get('f_name')
    #     l_name=request.POST.get('l_name')
    #     u_name=request.POST.get('u_name')
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')

    #     accounts=Accounts(F_NAME=f_name, L_NAME=l_name, U_NAME=u_name, EMAIL=email, PASSWORD=password)
    #     accounts.save()
    # if request.user.is_anonymous:
    #     return render(request, 'SIGNIN.html')
    if request.method=="POST":
        u_name=request.POST.get('u_name')
        password=request.POST.get('password')
        user=authenticate(username=u_name, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "Logged in successfully!")
            return redirect("/")
        return render(request, 'SIGNIN.html')
    elif request.user.is_authenticated:
        return redirect("/")
    return render(request, 'SIGNIN.html')

def check_password(pswd):
    special_character = ['`', '~', '!', '@', '#', '₹', '%', '^', '&', '*','(', ')', '_', '-', '+', '=', ',', '>', '<', '?', '/', '|', '$', '€', '{', '}', '[', ']', ';', ':', '.', '"', "'"]
    u,l,d,s = 0, 0,0,0
    if (len(pswd) >= 8):
        for i in pswd:
            if i.isalnum():
                if i.isupper():
                    u+=1
                elif i.islower():
                    l+=1
                elif i.isdigit():
                    d+=1
            else:
                for a in special_character:
                    if a in pswd:
                        s+=1
    if (u>0 and l>0 and d>0 and s>0):
        return 1
    else:
        return 0
    

def SIGNUP(request):
    if request.user.is_authenticated:
        return redirect("/")
    
    elif request.method=="POST":
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        u_name=request.POST.get('u_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if len(u_name)>10:
            messages.error(request,"Username must be under 10 characters.")
            return render(request,'SIGNUP.html')
        elif not u_name.isalnum() :
            messages.error(request,"Username only contains alphabets and numbers.")
            return render(request,'SIGNUP.html')
        elif User.objects.filter(username=u_name):
            messages.error(request,"This username exists try another one")
            return render(request,'SIGNUP.html')
        elif User.objects.filter(email=email):
            messages.error(request,"This email is already registered try another one")
            return render(request,'SIGNUP.html')
        elif password != confirm_password:
            messages.error(request,"Confirmation Password not matched")
            return render(request,'SIGNUP.html')
        elif not check_password(password):
            messages.error(request,"Your password in not secure.\nUse combination of special and alphanumeric characters whose size should be more than eight characters.")
            return render(request,'SIGNUP.html')

        user=User.objects.create_user(u_name, email, password)
        user.first_name=f_name
        user.last_name=l_name
        user.save()
        messages.success(request, "Account created succesfully!")
        return redirect('/signin')
    return render(request, 'SIGNUP.html')

def SIGNOUT(request):
    if request.method=="POST":
        logout(request)
    return redirect('/')

email=""
def resetemail(request):
    global email
    email=request.POST['email']


def logo_data():
    with open(finders.find('K:\ERUDITION\static\IMAGES\LOGO.png'), 'rb') as f:
        logo_data = f.read()
    logo = MIMEImage(logo_data)
    logo.add_header('Content-ID', '<logo>')
    return logo
def EMAIL_FOR_FORGOT_PASSWORD(request):
    if request.method=="POST":
        OneTimePassword()
        resetemail(request)
        if User.objects.filter(email=email):
            user=User.objects.get(email=email)
            msg_text=render_to_string('../templates/test.txt', {'VERIFICATION_CODE': Otp})
            msg_templ=render_to_string('../templates/mail.html', {'VERIFICATION_CODE': Otp})
            # send_mail('OTP VERIFICATION',
            # msg_text,
            # 'ynr24genius@gmail.com',
            # [email],
            # fail_silently=False,
            # html_message=msg_templ
            # )
            #I used EmailMultiAlternatives because I wanted to send both text and html
            emailMessage = EmailMultiAlternatives(subject="OTP VERIFICATION", body=msg_text, from_email='ynr24genius@gmail.com', to=[email], reply_to=[email])
            emailMessage.attach_alternative(msg_templ, "text/html")
            emailMessage.attach(logo_data())
            emailMessage.send(fail_silently=False)
            return render(request,'VERIFY.html')
        resetotp()
        return render(request, 'EMAIL_FOR_FORGOT_PASSWORD.html')

    if request.user.is_authenticated:
        return redirect("/")
    return render(request, 'EMAIL_FOR_FORGOT_PASSWORD.html')

Otp=""
def OneTimePassword():
    global Otp
    Otp=""
    for i in range(4):
        num=random.randint(0,9)
        Otp+=str(num)

def resetotp():
    global Otp
    Otp=""

def VERIFICATION(request):
    if request.method=="POST":
        OTP=request.POST.get('OTP')
        if OTP==Otp:
            resetotp()
            return render(request, 'RESET_PASSWORD.html')
        return render(request,'VERIFY.html')

    if request.user.is_authenticated:
        return redirect("/")
    return redirect("/forgot_password")

def RESET_PASSWORD(request):
    resetotp()
    if request.method=="POST":
        # try:
        user=User.objects.get(email=email)
        password=request.POST.get('password')
        user.set_password(password)
        user.save()
        return redirect('/')

    elif request.user.is_authenticated:
        return redirect("/")
    return redirect("/forgot_password")