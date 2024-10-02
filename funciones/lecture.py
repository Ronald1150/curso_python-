# #return devuelve valores que podre hacer uso
# #crear una funcion que retorne el numero 10 y muetra por terminal si es par
# # siempre que el valor que retorne mi funcion se utilize en mas sentencias u operaciones hacer de return 
# def diez():
#     return
# if diez()%2==0:
#     print("es par")
# else:
#     print("es par")
# #print solo muestra por terminal
# #return cuando queremos que nuestra funcion devuelva o retorne un tipo de dato o un tipo de dato estructurado
# # Crear una funcion que me muestre el producto de 2 numeros
# def producto(a,b):
#     return a*b

# # Carear una funcion que me retorne una lista de tres numeros 
# def lista_numeros():
#     return [3,2,6]
# #Crear una funcion que por en parametro reciba un nombre y retorne un nmensaje de bienvenida con el nombre
# # print usaremos cada vez que muestra funcion retorne un mensaje
# def mensaje(nombre):
#     print(f"hola,{nombre},bienvenido al chongo") 
# Crear una funcion que reciba por parametro una lista de numeros y me devuelva e l numero menor , mostrar por 
# el terminal el valor retornado por la funcion


lista=[4,3,6,78,7]
def Min(l):
    minimo=l[0]
    for n in l:
        if n <minimo:
            minimo=n
    return minimo
print(Min(lista))
#Crear una funcion que reciba comom parametro el nombre  y la edad de una persona mi funcion debera  retornar un 
# diccion con los datos, luego mostrar por terminal el valor de retorno de mi funcion
nombre="Ronald"
edad=19
def persona(nom,edad):
    return {
        "nombre":nom,
        "edad":edad
    }
print(persona(nombre,edad))