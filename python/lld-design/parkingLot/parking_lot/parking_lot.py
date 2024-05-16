import threading

class ParkingLot:
    instance = None

class __OnlyOne:
    def __init__(self, name, address):
        self.__name                 = name
        self.__address              = address
        self.__parking_rate         = ParkingRate()

        self.__compact_spot_count   = 0
        self.__large_spot_count     = 0
        self.__motorbike_spot_count = 0
        self.__electric_spot_count  = 0
        self.__max_compact_count    = 0
        self.__max_large_count      = 0
        self.__max_motorbike_count  = 0
        self.__max_electric_count   = 0

        self.__entrance_panels      = {}
        self.__exit_panels          = {}
        self.__parking_floors       = {}

        # all active parking tickets, identified by their ticket_number
        self.__active_tickets = {}

        self.__lock = threading.Lock()

    def __init__(self, name, address):
        None

    def __getattr__(self, name):
        None

    def get_new_parking_ticket(self, vehicle):
        None

    def is_full(self, type):
        None

    def increment_spot_count(self, type):
        None

    def is_full(self):
        None

    def add_parking_floor(self, floor):
        None

    def add_entrance_panel(self, entrance_panel):
        None

    def add_exit_panel(self,  exit_panel):
        None