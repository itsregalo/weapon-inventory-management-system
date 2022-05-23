
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import  send_mail
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_gen
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model

User = get_user_model()

"""for threading function where a user 
is told a function is complete while still loading
"""
import threading



# Create your views here.
# class EmailThread(threading.Thread):
#     def __init__(self, mail):
#         self.mail = mail
#         threading.Thread.__init__(self)
        
#     def run(self):
#         self.mail.send_mail()

        
def LogInView(request, *args, **kwargs):
    next_page = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if username == "":
            messages.error(request, "Username required")
        if password == "":
            messages.error(request, "Password is required")
        
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            messages.info(request, "You have successfully logged in")
            if next_page is not None:
                return HttpResponseRedirect(next_page)
            return redirect('core:index')
        else:
            messages.error(request,"invalid Login! Try again")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'auth/login.html', {})

def LogOutView(request, *args, **kwargs):
    logout(request)
    messages.success(request,"You successfully logged out")
    return redirect('core:index')


def RequestResetEmail(request):
    if request.method == 'POST':
        email = request.POST.get('email')
    
        user = User.objects.filter(email=email)
    
        if user.exists():
            uidb64 = urlsafe_base64_encode(force_bytes(user[0].pk))
            domain = get_current_site(request).domain #gives us the domain
            link = reverse('accounts:reset-password', 
                            kwargs={
                                'uidb64':uidb64, 
                                'token':PasswordResetTokenGenerator().make_token(user[0])
                                    })
            reset_password_url = f"http://{domain+link}"
            
            mail_subject = "Reset Password"

            
            mail_body = f"hi {user[0].username} click the link below to reset your password\n {reset_password_url}"
            mail = send_mail (mail_subject, mail_body,'noreply@courses.com',[email], fail_silently=False)
            messages.success(request, "Check your Email for the reset link")
            return redirect('accounts:login')
        else:
            messages.error(request, "Sorry, there is no user with that email")
            return redirect('accounts:request-reset-email')

    return render(request, 'auth/reset_email_form.html', {})
  
def ResetPasswordView(request, uidb64, token):
    
    if request.method == 'POST':
        context = {
            'uidb64':uidb64,
            'token':token,
        }
        
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        
        if password1 == "":
            messages.error(request, "Password is required")
        if password2 == "":
            messages.error(request, "Repeat Password is required")
            return render(request, 'auth/reset_password.html', context)
        if password1 != password2:
            messages.error(request, "Passwords do not match")
        if len(password1)<6:
            messages.error(request,"Password is too short")
            return render(request, 'auth/reset_password.html', context)
        if password1 != password2:
            messages.error(request, "Passwords do not match")
        if len(password1)<6:
            messages.error(request,"Password is too short")
            return render(request, 'auth/reset_password.html', context)  
        
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
            user.set_password(password1)
            user.save()
            messages.success(request, "password changed successfully")
            return redirect('accounts:login')
        except DjangoUnicodeDecodeError as identifier:
            messages.error(request, "oops! something went wrong")
            return render(request, 'auth/reset_password.html', context)
        
    context = {
        'uidb64':uidb64, 
        'token':token
        }
        
    try:
        user_id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=user_id)
        
        if not PasswordResetTokenGenerator().check_token(user, token):
            messages.error(request, "Opps, The link has expired")
            return render(request, 'auth/reset_email_form.html')
        
        messages.success(request, "verified")
        return render(request, 'auth/reset_password.html', context)
    except DjangoUnicodeDecodeError as identifier:
        messages.error(request, "oops! something went wrong")
        return render(request, 'auth/reset_email_form.html', context)