from web_chat.dto import PersonDTO


class PersonConvertor:
    @staticmethod
    def convert_entity_to_dto(person):
        return PersonDTO(person.name, person.login, person.role.role_name)