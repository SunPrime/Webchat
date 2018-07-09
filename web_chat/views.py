from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from helper import RegistrationHelper, LoginHelper
from web_chat.forms import RegistrationForm


class Index(View):
    def get(self, request):
        return render(request, 'index.html', {'login': reverse('login'), 'registration': reverse('registration')})


class Login(View):
    def get(self, request):
        error = request.session.get('error')
        if error == None:
            error = ''
        else:
            request.session['error'] = None
        return render(request, 'login.html', {'error': error})

    def post(self, request):
        login = request.POST.get('login')
        password = request.POST.get('password')

        if login == None or password == None:
            error = "Login or password cannot be Null"
            request.session['error'] = error
            return redirect(reverse('login'))
        person_dto = LoginHelper.checklogin(login, password)

        if person_dto == None:
            error = "Login or password incorrect"
            request.session['error'] = error
            return redirect(reverse('login'))

        request.session['login'] = person_dto.login
        request.session['role'] = person_dto.role_name
        if person_dto.role_name == 'user':
            return redirect(reverse('chat'))
        else:
            return redirect(reverse('admin'))


class Registration(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def post(self, request):
        reg_form = RegistrationForm(request.POST)
        if RegistrationHelper.save(reg_form):
            return redirect(reverse('index'))
        else:
            return render(request, 'registration.html', {'form': reg_form})


class Chat(View):
    pass


class Admin(View):
    def get(self, request):
        if request.session.get('role') == 'admin':
            return render(request, 'admin.html', {'url_get_user': reverse('getuser')})
        return redirect(reverse('index'))