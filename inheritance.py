class Country:
    
    def primeMinister(self):
        print("Narendra Modi")
    
    def language(self):
        print("Hindi")
        

class States(Country):
    
    def chiefMinister(self):
        print("Jagan Mohan Reddy")
    
    def language(self):
        print("Telegu")
    
    def __statesCap(self):
        print("Amaravati")
        
class City(States):
    
    def Mayor(self):
        print("Sujatha")

# c = Country()
# s = States()

# # c.primeMinister()
# s.primeMinister()
# s.chiefMinister()

c = City()

c.primeMinister()
c.chiefMinister()
c.Mayor()


s = States()
s.language() 