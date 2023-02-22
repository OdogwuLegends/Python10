from AccountType import AccountType
from data.model.AccountType import AccountType


class Account(object):
    def __init__(self):
        self._account_id: int = 0
        self._pin = None
        self._card_number = None
        self._bank = None
        self._account_type = AccountType()
        self._account_number = None
        self._account_user = None
        self._transfer_limit = None
        self._account_limit = None

    def set_account_id(self, account_id):
        self._account_id = account_id

    def get_account_id(self):
        return self._account_id

    def withdraw(self):
        pass

    def deposit(self):
        pass

    @set_pin.setter
    def set_pin(self, pin) -> None:
        self._pin = pin

    def set_card_number(self, card_number) -> None:
        self._card_number = card_number

    def get_card_number(self) -> None:
        return self._card_number

    def set_account_number(self, account_number: str) -> None:
        self._account_number = account_number

    def get_account_number(self):
        return self._account_number

    def set_account_type(self, account_type) -> None:
        self._account_type = account_type

    def get_account_type(self) -> AccountType:
        return self._account_type

    def set_account_limit(self, account_limit) -> None:
        self._account_limit = account_limit

    def get_account_limit(self):
        return self._account_limit

    def set_account_user(self, account_user) -> None:
        self._account_user = account_user

    def get_account_user(self):
        return self._account_user

    def set_transfer_limit(self, transfer_limit) -> None:
        self._transfer_limit = transfer_limit

    def get_transfer_limit(self):
        return self._transfer_limit
