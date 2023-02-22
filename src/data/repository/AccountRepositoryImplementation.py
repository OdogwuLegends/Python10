from data.model.Account import Account
from data.model.PersonalInformation import PersonalInformation
from data.model.User import User
from data.repository.AccountRepositoryInterface import AccountRepositoryInterface


class AccountRepositoryImp(AccountRepositoryInterface):
    account_data_base = {}
    account_id_count: int = 0
    account = Account()
    personal_info = PersonalInformation()
    user = User()

    def create_new_account(self, first_name, last_name, mobile_number, gender, relationship, lga, state, email):
        self.account.set_account_id(self.account_id_count + 1)
        self.personal_info.set_first_name(first_name)
        self.personal_info.set_last_name(last_name)
        self.personal_info.set_email_address(email)
        self.personal_info.set_mobile_number(mobile_number)
        self.personal_info.set_local_govt(lga)
        self.personal_info.set_state_of_origin(state)
        self.user.set_personal_info(self.personal_info)
        self.account.set_account_user(self.user)

        self.account_data_base[set.account.get_account_id()] = self.account
        return self.account_data_base

    def deposit(self, amount):
        pass

    def withdraw(self, amount, pin):
        pass

    def transfer(self, amount, account_name, account_number, bank_name, pin):
        pass

    def check_balance(self, account_number, pin):
        pass


if __name__ == '__main__':
    acc_impl = AccountRepositoryImp()
    acc_impl.create_new_account("Elite", "C15", "09087654321", 56, "Female", "single", "Eko", "Lagos", )
