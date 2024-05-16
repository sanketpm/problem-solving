class ParkingDisplayBoard:
    def __init__(self, id):
        self.__id = id
        self.__handicapped_free_spot = None
        self.__compact_free_spot = None
        self.__large_free_spot = None
        self.__motorbike_free_spot = None
        self.__electric_free_spot = None
    
    def show_empty_spot_number(self):
        None