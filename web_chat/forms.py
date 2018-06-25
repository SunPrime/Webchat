from django.forms import ModelForm, PasswordInput

from web_chat.models import Person


class RegistrationForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'login', 'password']
        widgets = {'password': PasswordInput(),}