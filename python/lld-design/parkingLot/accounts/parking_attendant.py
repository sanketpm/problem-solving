from account import Account
from enums import AccountStatus

class ParkingAttendant(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        super().__init__(user_name, password, person, status)
    
    def process_ticket(self, ticket_number):
        None
