# company - sample1
class Company:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
    
    def show(self):
        print(f"{self.name}__{self.location}")

elxsi = Company('Tata Elxsi', 'Bengaluru')
google = Company('Google', 'California')

elxsi.show()
google.show()

print()
# company - sample 2
class Company:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
    
    def show(self):
        print(self.name,"--",self.location)

elxsi = Company('Tata Elxsi', 'Bengaluru')
google = Company('Google', 'California')

elxsi.show()
google.show()

