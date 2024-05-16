from enums import AccountStatus

class Account:
    def __init__(self, user_name, password, person, status = AccountStatus.ACTIVE):
        self.__user_name = user_name
        self.__password = password
        self.__person = person
        self.__status = status
    
    def reset_password(self):
        None