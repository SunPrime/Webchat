from django.db import transaction

from web_chat.covertors import PersonConvertor
from web_chat.models import Person


class RegistrationHelper:
    @staticmethod
    def save(reg_form):
        if reg_form.is_valid():
            name = reg_form.cleaned_data['name']
            login = reg_form.cleaned_data['login']
            password = reg_form.cleaned_data['password']
            person = Person(name=name, login=login, password=password, role_id=1)
            try:
                person.save()
                return True
            except ValueError:
                return False
        return False


class LoginHelper:
    @staticmethod
    @transaction.atomic
    def checklogin(login, password):
        person = Person.objects.filter(login=login, password=password).first()
        if person == None:
            return None
        else:
            return PersonConvertor.convert_entity_to_dto(person)
