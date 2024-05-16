'''
Creational Pattern: Builder
- use builder over factory almost always
- Gives control to programmer over the object data values

Used this pattern a lot with ProtoBuf in Google
'''

class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None
    
    def setBuns(self, bun_style):
        self.buns = bun_style
    
    def setPatty(self, patty_style):
        self.patty = patty_style
    
    def setCheese(self, cheese_style):
        self.cheese = cheese_style
    
    def print(self):
        print(f'{self.buns} , {self.patty} , {self.cheese}')

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()
    
    def add_buns(self, bun_style):
        self.burger.setBuns(bun_style)
        return self
    
    def add_patty(self, patty_style):
        self.burger.setPatty(patty_style)
        return self

    def add_cheese(self, cheese_sytle):
        self.burger.setCheese(cheese_sytle)
        return self

    def build(self):
        return self.burger

burger = BurgerBuilder() \
            .add_buns('sesame') \
            .add_patty('fish-patty') \
            .add_cheese('swiss chesse') \
            .build()

burger.print()