from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views import View

# from django.auth.models import User
from .forms import UserAuthenticationForm,UserRegistrationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import MyUser

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class LoginPageView(View):
    form_class = UserAuthenticationForm
    template_name = 'auth/login.html'
    
    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        # <process form cleaned data>
        form =self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(email=email, password=password)
            if user is not None:
                # return render(request,'dashboard/index.html')
                login(request, user)
                if user.is_superuser:
                    return redirect("/admin/")
                else:
                    return redirect("/dashboard/")
            else:
                messages.warning(request,f'Invalid Email/Password')
                return redirect('user:login')
        else:
            messages.warning(request,form.errors)
            return redirect('user:login')


class LogoutPageView(View):
    template_name = 'auth/logout.html'

    def get(self,request):
        logout(request)
        return redirect('/')



class RegisterPageView(View):
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'

    def get(self,request):
        user = request.user
        if user.is_authenticated: 
            logout(request)
        return render(request,self.template_name,{'form':self.form_class})

    def post(self, request, *args, **kwargs):
        form =self.form_class(request.POST)

        email = request.POST['email']
        
        if (request.POST['password1']==request.POST['password2']):
            if (MyUser.objects.filter(email=email)):
                messages.warning(request,f'Email Already exists.')
            else:
                if form.is_valid():
                    form.save()
                    messages.success(request,f'Your Account has been created you can Login now!')
                else:
                    messages.warning(request,form.errors)
        else:
            messages.warning(request,f'Password Mismatch')
        return redirect('user:register')



class HomePageView(LoginRequiredMixin,View):
    form_class = UserAuthenticationForm
    template_name = 'dashboard/index.html'
    

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'auth/password_reset.html'
    email_template_name = 'auth/password_reset_email.html'
    subject_template_name = 'auth/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('user:index')