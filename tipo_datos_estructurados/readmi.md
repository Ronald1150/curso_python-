# TIPOS DE DATOS ESCTRUCTURADOS (TDA-tipos de datos estructurados)
```python
#Lista-sus valores o elementos se pueden actualizar,
#eliminar
lista=["nombre",20,5.2,.5,False,["texto",.2]]
#tupla - sus valores o elementos no pueden ser modificadoso eliminados.

tupla=("abel",20,5.2,False,[])
#diccionario o objetos-Los diccionario almacena los datos con clave:valor
diccionario={"nombre":"antonio","edad":15,"sexo":False}
-[!TIP]
**Observacion:** que los tipos de datos estructurados pueden almacenar en su interior otros tipos de datos estructurados.
```
```python
lista_alumnos=[
    {
        "nombre":"ruth",
        "edad":20
        "amigos":["flor","rocio"]
    },{
        "nombre":"abel"
        "edad":20
        "amigos":["no_tiene"]
    },{
        "nombre":"jose ma"
        "edad":17
    },{
        "nombre":"ronny"
        "edad":15
    }
]
##metodos
###1.-convertir texto a lista
```python
texto="hola"
list(texto)
#["h","o","i","a"]
##metodo split
texto="hola_como_estan_alumnitos_lindos"
texto.split(",")
```
##metodo join 
```python
texto_largo="hola como estan bienvenidosal salon"
nueva_lista=texto_largo.split("")
print("".join(nnueva_lista))
### 2 agregar agregar elementos al final de una lista
#metodo append- es el metodo que me permite agrega elementos al final de  una lista
lista=["hola"]
lista.append("mundo")
#["hola","mundo"]
#metodo insert - es el metodo que eme permite agrega elementos en cualquier ubicasion de mi lista
lista_nombre=["edith","ruth","luz"]
lista_nombre.insert(0,"anthony")
### 3.-eliminar elementos  de una lista
 ```python 
 #metodo pop - es el metodo que elimina el ultimo elemento de una lista es el contrario de append
 lista_nombre=["edith","ruth","luz"]
  lista_nombre.pop()
  #metodo -remove.- este metodo elimina el por el nombre del elemento que conicidad dentro de mi lista.
  lista_nombre=["edith","ruth","luz"]
  lista_nombre.remove("ruth")
  ##segunda opsion- metodo pop al pasarle poe el parametro un indice este lo elimina de la lista.
  lista_nombre=["edith","ruth","luz"]
  lista_nombre.pop(0)
#4.- buscar un elemento en una lista
```python
lista_nombre=["edith","ruth","luz"]
indice=lista_nombres.index("ruth")
print(lista_nombre[indice])
## 5.-Comparacion de listas
#pódemos hacer uso de los operadores de comparacion para comparar listas
**ejem**
```python
compara=[1,2,3]>[1,2,4]
#1 no por QUE son iguales en ambas lista
#2no por que son iguales en ambas listas
#3 evalua que ws menor a 4
# entonses la primera lista es menor que la segunda lista
print(compara)
#salida
```
###7.- fe de erratas(actualizar lista)
```python
lista=[1,3,4,5,6]
lista[0]=2
print(lista)
alumnos[
    {
        "nombre":"abel",
        "edad":15
    },
    {
        "nombre":"anthony",
        "edad":29
    }
]
alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15}
print(alumnos)
#8 .listas y diccionario por comprencion
#es una tecnica pythonica que nos permite crear listas y diccionarios en una sola linea combinando bucles y diccionario
[!NOTE]
**VLC** VALUE LOOP CONDITION- valor condicion 
```python
# lista por comprencion
texto="1,4,8,9,6"
nueva_lista=[int(n) for n in texto.split(",") if int (n)%2==0]
print(nueva_lista)
#diccionario por comprencion
lista_amigo=["abel","anthony","edith","ruth"]
diccionario={amigo:len(amigo) for amigo in lista_amigo}
print(diccionario)
f