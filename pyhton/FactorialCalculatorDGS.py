def factorial (number):
    if(type(number)!=int):
        raise Exception ("Esta funcion solo acepta números")
    else:
        if(number<0):
            raise Exception ("No se pueden pasar números menores que 0")
        else:
            resultado=1
            for i in range(1,number+1):
                resultado=resultado*i
            return resultado
        
try:
    print(factorial("Coc"))
except Exception as erro:
    print(erro)

try:
    print(factorial(-4))
except Exception as erro:
    print(erro)

try:
    print(factorial(6))
except Exception as erro:
    print(erro)
