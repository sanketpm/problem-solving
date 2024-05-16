'''
       cheese ['bun', 'cheese', 'beef-patty']
deluxe-cheese ['bun', 'tomato', 'lettuce', 'cheese', 'beef-patty']
       veggie ['bun', 'special-sauce', 'veggie-patty']
'''

class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def print(self):
        print(self.ingredients)


class BurgerFactory:
    def createCheeseBurger(self):
        return Burger(['bun', 'cheese', 'beef-patty'])
    
    def createDeluxeCheeseBurger(self):
        return Burger(['bun', 'tomato', 'lettuce', 'cheese', 'beef-patty'])

    def createVeganBurger(self):
        return Burger(['bun', 'special-sauce', 'veggie-patty'])

burgerFactory = BurgerFactory()

burgerFactory.createCheeseBurger().print()
burgerFactory.createDeluxeCheeseBurger().print()
burgerFactory.().print()