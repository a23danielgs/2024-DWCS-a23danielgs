class calculator:
    numberOfObjects=0

    def __init__(self,num1=None,num2=None):
        if(num1==None):
            num1=0
        if(num2==None):
            num2=0

        if(type(num1)!=int):
            raise Exception("Num1 must be an integer")
        elif(type(num2)!=int):
            raise Exception("Num2 must be an integer")
        else:
            self.num1=num1
            self.num2=num2
            calculator.numberOfObjects+=1


    def __str__(self):
        return f"Num1:{self.num1}   Num2:{self.num2}    Number Of Objects:{calculator.numberOfObjects}"
    
    def suma(self):
        suma = self.num1+self.num2
        return f"Suma:{suma}"
    
firstCalcule = calculator ()
firstCalcule.num1 = 5
firstCalcule.num2 = 6
print(f"el número uno => {firstCalcule.num1}    el segundo número => {firstCalcule.num2}")

secondCalcule = calculator (10,20)
print(secondCalcule)
print(secondCalcule.suma())
print(firstCalcule.suma())

try:
    thirdCalcule = calculator("",8)
except Exception as erro:
    print(erro)

try:
    thirdCalcule = calculator(8,"")
except Exception as erro:
    print(erro)

