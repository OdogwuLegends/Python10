from data.model.PersonalInformation import PersonalInformation


class User:
    def __init__(self):
        self._next_of_kin = NextOfKin()
        self._user_address = Address()
        self._user_personal_information = PersonalInformation()

    def set_personal_info(self, personal_info):
        self._user_personal_information = personal_info

    def get_personal_info(self, ):
