def person (age,name,surname="Apelido"):
    if(name == None):
        print(f"{surname} is {age} years old.")
    else:
        print(f"{name} {surname} is {age} years old.")

person(5,"Alejandro","Fraga")
person(7,"Diego")
person(85)