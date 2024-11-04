##Class Alien
class Alien:
    numberOfAliens = 0
    def __init__(self,name):
        self.name = name
        Alien.numberOfAliens+=1

    def __del__(self):
        Alien.numberOfAliens-=1
        

    def getNumberOfAliens():
        return Alien.numberOfAliens

    def __str__(self):
        return f"Name : {self.name}"
    
##CODE

Al1=Alien("Pedro")
Al2=Alien("Jorge")
Al3=Alien("Blorp")

print(Alien.getNumberOfAliens())

Al4=Alien("Blerp")

print(Alien.getNumberOfAliens())

del Al2

print(Alien.getNumberOfAliens())
