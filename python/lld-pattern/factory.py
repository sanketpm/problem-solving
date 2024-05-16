# Creational : Factory
'''
1. Class that receives some params to create object, 
    - you can send any data to the params & create an items,
    - over time you observe that you basically send the same data to params to create objects
    - you club these datas & create a Factory Class
    - the factory class exposes methods with has the data saved
    - just calling the corresponding method of factory class will get you your desired object

problems:
    - Initially it feels nice to just call a factory over time you forget as to what data the factory method is adding
    - No control over the param-values when you call factory methods cuz it does the job for you & you're blocked from editing it
'''

class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ['bun', 'cheese', 'beef-patty']
        return Burger(ingredients)

    def createDeluxeCheeseBurger(self):
        ingredients = ['bun', 'tomato', 'lettuce', 'cheese', 'beef-patty']
        return Burger(ingredients)

    def createVeganBurger(self):
        ingredients = ['bun', 'special-sauce', 'veggie-patty']
        return Burger(ingredients)

burgerFactory = BurgerFactory()

burgerFactory.createCheeseBurger().print()
burgerFactory.createDeluxeCheeseBurger().print()
burgerFactory.createVeganBurger().print()