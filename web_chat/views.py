from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView

from helper import RegistrationHelper
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


class Registration(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def post(self, request):
        reg_form = RegistrationForm(request.POST)
        if RegistrationHelper.save(reg_form):
            return redirect(reverse('index'))
        else:
            return render(request, 'registration.html', {'form': reg_form})