from web_chat.models import Person


class RegistrationHelper:
    @staticmethod
    def save(reg_form):
        if reg_form.is_valid():
            name = reg_form.cleaned_data['name']
            login = reg_form.cleaned_data['login']
            password = reg_form.cleaned_data['password']
            person = Person(name= name, login= login, password= password, role_id = 1)
            try:
                person.save()
                return True
            except ValueError:
                return False
        return False
