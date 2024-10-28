class Dog:
        
    def __init__(self,name,age,furcolor):
        self.name=name
        self.age = age
        self.furcolor = furcolor

    dogInfo="Dogs can and will lick their balls!"
    
    def Bark(self):
        print("GUAU!")

mydog = Dog("Mierdon","43","Negro")
mydog.Bark()
""" mydog.name = "Fido" """
""" mydog.age = 16 """
print(mydog.name)
print(mydog.age)

Dog.dogInfo="Hey there I'm dogging doggity dog"
print(Dog.dogInfo)