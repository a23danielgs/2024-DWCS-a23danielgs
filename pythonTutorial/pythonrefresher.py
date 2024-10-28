age = 49
name = "Matt"
name22 = 'Nick'

# COMENTARIO

print("Hello world")
print(f"Hello my name is {name} and I am {age} years old")
print("Hello my name is {} and i am {} years old".format(name,age)) 

if age > 18:
    print("You are older than 18")
    print("Bla Bla")
else:
    print("You are younger than 18")

todayIsCold = False

if todayIsCold:
    print("Tengo frio en las ****")
else:
    print("Tengo las **** sudadas")

# CHALLENGE 1 : 

year = 1830
if (year > 2000 and year < 2099):
    print("Welcome to the 21st century!")
else:
    print("Go fuck yourself")

def hello(thestring="Default - Name", theOtherString = 0):
    print(f"Hello, {thestring} you are {theOtherString}")

hello(name,age)