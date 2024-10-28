def factorial (number):
    if(type(number)!=int):
        raise Exception ("This function only accepts numbers")
    elif(number<0):
            raise Exception ("You can´t pass a number lesser than 0")
    else:
        resultado=1
        for i in range(1,number+1):
            resultado=resultado*i
        return resultado
        
try:
    print(factorial("Croac"))
except Exception as erro:
    print(erro)

try:
    print(factorial(-4))
except Exception as erro:
    print(erro)

try:
    print(factorial(0))
except Exception as erro:
    print(erro)

try:
    print(factorial(6))
except Exception as erro:
    print(erro)
