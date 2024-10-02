#crear un lista de 5 alumnos almacenar su nombre
#apellido y edad
#insertar al final de la lista los datos de antony
#eliminar de la lista si exsiste lo datos de abel
#buscar y mostrar el alumno en la pocision 4 de  la lista
# 2.-crear una lista con 4 dicionario donde tendran los datos de sus mascotas (nombre,edad,sexo,raza)
#tareas
#mostrar la lista con 4 diccionario
#
# Un empresario de alquiler de autos desea guardar en una base de datos la informacion de sus vehiculos , proceso
# que desea authomatizar con un sistema informatico, las acciones que puede realizar el empresario son ver la lista 
# de autos que tiene, podra tambien actualizar y agregar un nuevo vehiculo
#caso de uso
# programacion
# lista_1={     "nombre":"ronald",
#               "apellido":"valencia",
#               "edad":18
#         },{
#              "nombre":"michael",
#              "apellido":"romero",
#              "edad":16
#         },{
#              "nombre":"juan",
#              "apellido":"gutierres",
#              "edad":19
#         },{
#              "nombre":"marco",
#              "apellido":"anampa",
#              "edad":15
#         },{
#              "nombre":"niko",
#              "apellido":"belick",
#              "edad":23
#         }
# lista_1.insert(0,"niko")

#lisyta de los primeros 30 numeros primos usando comprension de lista 
for lista_numeros in range(1,100):
    lista_nueva=[int(n) for n in lista_numeros.split(",") if int (n)%2==0]
    print(lista_nueva)
#diccionario por comprencion 
# nueva_amigos=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
# diccionario={}
# for _,v in enumerate(nueva_amigos):
#     diccionario[v]=len(v)