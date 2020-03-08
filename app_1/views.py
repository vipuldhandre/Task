import random
import string

from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth import authenticate, logout, login

from .forms import *
from .signals import *

# Create your views here.


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class Index(View):
    template_name = 'profile.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/')
        user_profile = UserProfile.objects.filter(user=request.user)
        return render(request, self.template_name, {'data': user_profile})


class UploadDoc(View):
    template_name = 'upload_doc.html'
    form_class = ProfileForm

    def get(self, request):
        form = self.form_class()
        if not request.user.is_authenticated:
            return redirect('/')
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('/')

        print('request.FILES: ', request.FILES)
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/index/')

        return render(request, self.template_name, {'form': form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class Login(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/index/')
        return render(request, self.template_name)

    def post(self, request):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user=user)
            return redirect('/index/')
        return render(request, self.template_name, {'error': 'unauthenticated user.'})


class Registration(View):
    template_name = 'registration.html'
    form_class = UserForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        letters = string.ascii_lowercase + string.ascii_uppercase
        password = ''.join(random.choice(letters) for i in range(6))

        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(password)
            print(user)
            user.save()
            is_sent = send_mail(
                subject='your password!',
                message='welcome, your username: '+request.POST['username']+' and password: '+password,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.POST.get('email', '')],
                fail_silently=True
            )
            print('is_sent: ', is_sent)
            return redirect('/login/')
        else:
            return render(request, self.template_name, {'form':form})
