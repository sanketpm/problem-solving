from abc import ABC
from enums import ParkingSpotType

class ParkingSpot(ABC):
    def __init__(self, number, parking_spot_type):
        self.__number = number
        self.__parking_spot_type = parking_spot_type
        self.__free = True
        self.__vehicle = None
    
    def get_number(self):
        return self.__number
    
    def get_type(self):
        return self.__parking_spot_type
    
    def is_free(self):
        return self.__free
    
    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        self.__free = False
    
    def remove_vehicle(self):
        self.__vehicle = None
        self.__free = True

class HandicappedSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.HANDICAPPED)

class CompactSport(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)

class LargeSport(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)

class MotorbikeSport(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.MOTORBIKE)

class ElectricSport(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)