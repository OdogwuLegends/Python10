from typing import Type

from data.model.Gender import Gender
from data.model.RelationshipStatus import RelationshipStatus
from data.model.Country import Country


class PersonalInformation:
    def __init__(self):
        self._person_id: int = 0
        self._first_name: str = ""
        self._last_name: str = ""
        self._gender = Gender()
        self._relationship_status = RelationshipStatus()
        self._mobile_number = None
        self._country_code = Country
        self._local_government = None
        self._state_of_origin = None
        self._email_address = None

    def set_email_address(self, email: str) -> None:
        self._email_address = email

    def get_email_address(self) -> str:
        return self._email_address

    def set_state_of_origin(self, state: str) -> None:
        self._state_of_origin = state

    def get_state_of_origin(self) -> str:
        return self._state_of_origin

    def set_local_govt(self, lga: str) -> None:
        self._local_government = lga

    def get_local_govt(self) -> str:
        return self._local_government

    def set_mobile_number(self, number: str) -> None:
        self._mobile_number = number

    def get_mobile_number(self) -> str:
        return self._mobile_number

    def set_full_name(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    def set_first_name(self, first_name) -> None:
        self._first_name = first_name

    def _get_first_name(self):
        return self._first_name

    def set_last_name(self, last_name) -> None:
        self._last_name = last_name

    def _get_last_name(self):
        return self._last_name

    def set_country_code(self, code) -> None:
        self._country_code = code

    def get_country_code(self) -> Type[Country]:
        return self._country_code

    def set_person_id(self, person_id):
        self._person_id = person_id

    def get_person_id(self):
        return self._person_id


if __name__ == '__main__':
    per = PersonalInformation()
    country = Country
    per.set_country_code(country.FRANCE.value)
    print(per.get_country_code())
