def potencia(base,exponente):
    if(type(base)!=int or type(exponente)!=int):
         raise Exception("Esta funcion solo acepta números")
    else:
        resultado=1
        for i in range(0,exponente):
            resultado = resultado*base
        return resultado
    
try:
    print(potencia("x","y"))
    print(potencia(2,5))
except Exception as erro:
    print(erro)


    

