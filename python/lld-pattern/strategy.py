'''
If you want to modify the behaviour of the class
without changing it use Strategy Pattern (Behavioural Pattern)

(+) We want to comply to this principle
    >> Open Closed Principle
    >>__ Open for extension
    >>__ closed for modification


Make the damn thing you want into an interface, & do the logic below it (child classes)
Program at an interface level that is what is means

'''

'''
Revision:
- Forgot to have ABC for strategies

'''

from abc import ABC, abstractmethod

class FilterStrategy:
    @abstractmethod
    def removeValue(self, val):
        pass

class RemoveNegativeStrategy:
    def removeValue(self, val):
        return val < 0
    
class RemoveOddStrategy:
    def removeValue(self, val):
        return bool(abs(val) & 1)

class Array:
    def __init__(self, arr):
        self.arr = arr
    
    def filter(self, strategy):
        res = []

        for val in self.arr:
            if not strategy.removeValue(val):
                res.append(val)
        return res

values = Array([-7, -4, -1, 0, 2, 6, 9])

pos_values = values.filter(RemoveNegativeStrategy())
even_values = values.filter(RemoveOddStrategy())

print(pos_values)
print(even_values)