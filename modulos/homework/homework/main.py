"""# este es el script"""
def mayor_edad(edad):
    """funcion para saber si una persona es mayor de edad
    """
    if edad >=18:
        print("es mayor de edad")
    else:
        print("es menor de edad")
def es_menor(lista):
    """funcion para saber el numero mayor de una lista"""
    mayor=lista[0]
    for n in lista:
        if n> mayor:
            menor=n
    return menor

def es_mayor(lista):
    """funcion para saber el numero mayor de una lista"""
    mayor=lista[0]
    for n in lista:
        if n > mayor:
            mayor=n 
    return mayor



def cuenta_vocales(text:str):
    """funcion para contar la cantidad de vocales a que aparecen en un texto"""
    text_minusculas:str=text.lowwer()
    cantidad_vocales=0
    for n in text_minusculas:
        if n == "a":
            cantidad_vocales+=1
    return cantidad_vocales


mayor_edad(20)
print(es_mayor([4,5,2,4,5,6,]))
print(cuenta_vocales("mi mama me mima yo amo a mi mama"))



"""# este es el script principal"""
