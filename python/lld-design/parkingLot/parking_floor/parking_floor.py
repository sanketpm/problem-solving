from enums import ParkingSpotType
from parking_spot import parking_spot
from parking_display_board import parking_display_board

class ParkingFloor:
    def __init__(self, name):
        self.__name = name
        self.__handicapped_spots = {}
        self.__compact_spots = {}
        self.__large_spots = {}
        self.__motorbike_spots = {}
        self.__electric_spots = {}
        self.__info_panels = {}
        self.__display_board = parking_display_board.ParkingDisplayBoard()
    
    def add_parking_spot(self, spot: parking_spot.ParkingSpot):
        None
        
    def assign_vehicle_to_spot(self, vehicle, spot: parking_spot.ParkingSpot):
        None
    
    def free_spot(self, spot):
        None
    
    def update_board_for_handicapped(self, spot):
        None

    def update_board_for_compact(self, spot):
        None