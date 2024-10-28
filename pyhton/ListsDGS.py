""" Create a page with two functions:

1. tripleCheck

This function receives a list of integers and returns a boolean indicating if a triple is present in that array or not. If a value appears three times in a row in an array it is called a triple.

Sample Input:
{ 1, 1, 2, 2, 1 }
{ 1, 1, 2, 1, 2, 3 }
{ 1, 1, 1, 2, 2, 2, 1 }
Sample Output:
bool(false)
bool(false)
bool(true) """

def tripleCheck (numbers):
    Check=0
    contador=0
    for i in numbers:
        if (numbers[i] == Check):
            contador=contador+1
            if(contador>2):
                return True
        else:
            contador = 0
        Check=numbers[i]
    return False

print(f"1bool({tripleCheck([ 1, 1, 2, 2, 1 ])})")
print(f"2bool({tripleCheck([ 1, 1, 2, 1, 2, 3 ])})")
print(f"3bool({tripleCheck([ 1, 1, 1, 2, 2, 2, 1 ])})")

""" 2. countries 

This function receives a list with pairs country - capital and shows a description on the screen as below: """

ceu = { "Italy":"Rome", "Luxembourg":"Luxembourg", "Belgium":"Brussels", "Denmark":"Copenhagen", "Finland":"Helsinki", "France":"Paris", "Slovakia":"Bratislava", "Slovenia":"Ljubljana", "Germany":"Berlin", "Greece":"Athens", "Ireland":"Dublin", "Netherlands":"Amsterdam", "Portugal":"Lisbon", "Spain":"Madrid", "Sweden":"Stockholm", "United Kingdom":"London", "Cyprus":"Nicosia", "Lithuania":"Vilnius", "Czech Republic":"Prague", "Estonia":"Tallin", "Hungary":"Budapest", "Latvia":"Riga", "Malta":"Valetta", "Austria" : "Vienna", "Poland":"Warsaw" }

""" Sample Output :

The capital of Netherlands is Amsterdam 
The capital of Greece is Athens 
The capital of Germany is Berlin  """

def countries (Paises):
    for Pais,Capital in Paises.items():
        print (f"The capital of {Pais} is {Capital} ")

countries(ceu)
