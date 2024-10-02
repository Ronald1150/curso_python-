# FUNCIONES
Matematicamente una funcion es una operacion que toma uno o mas valores llamados `argumentos` y produce un valor denominado `resultado`
>[!NOTE]
>Todos los lenguajes de programacion tienen funciones incorporadas (`funciones internas`), y funciones creadas por el usuario(`funciones externas`)


En programacion una funcion es unn sub programa ,es una escritura que nos permite agrupar codigo y sus principales objetivos son:
-`NO REPETIR` fracmentos de codigo
-`REUTILIZAR` el codigo en distitos escenarios
## Estructura de una funcion
Una funcion viene `definida` por un `nombre`, sus `parametros` y su valor de `retorno`.
Una ves creada la funcion podremos solicitar su ejecusion su ejecusion `invocando` la funcion por su nombre `nombre`
## Definir una funcion en python
Para definir una funcion en python primero utilizaremos la palabra reservada  `def` seguida por el `nombre` de la funcion. A continuacion especificaremos los `parametros` con `()` si es una funcion sin  parametros ,`(a)` si es una funcion con parametros, si se tuvira mas de un  parametros iran separados por `,` , finalizaremos la linea con `:` , en al siguiente linea sin  olvidar el identado, comensara el `cuerpo` de la funcion (micro programa) que puede contener 1 o mas sentencias, finalmete devera `retornar` un resultado con la palabra reservadad `return`.
***
>[!TIP]
>Como tambien se puede utilizar la `funcion interna` , `print` `()` para depuracion de codigo no es rercomendable usarlo en produccion.


## `print` 
Es una herramienta de depuracion para depurar o comprovar si una funcion esta aciendo los correcto 

**Ejemplo:**
```python
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    return f"{saludo},{saludo_dos}"
    #print(f"{saludo},{saludo_dos}")
print(saludo())
```
## Invocar una funcion
Para invocar una funcion,(o llamar, ejecutar)una funcion solo tendremos que escribir el `nombre` de la funcion seguido por `()` parentesis.
```python
def saludo():
    print("hola")
#invocando la funcion
saludo()
```

## Retornar un valor
Las funciones pueden retornar (o devolver) un valor.
```python
def uno():
    return 1
uno()
```

>[!WARNING]
>No confundir `print()` con `return` . El valor retornado por `return` nos permite usarlo fuera de su contexto, y `print` solo mostrara el literal por terminal.
**Ejemplo:**
```python
*en el archivo `lectura.py`
```

## Retornado multiples valores 
El secreto es hacerlo mediante un tipo de dato estructurado
```python
def tupla():
    return 2,3,4
varios()
#retorna (2,3,4)
def lista():
    return ["hola",45]
lista()
# retorna ["hola",45]
def dicc():
    return{"nombre",}
```
# Parametros y argumentos
si un parametro no dispusiera de valores de entrada estaria limitadad en su actuacion .
Es por ello que los `parameros` no permiten variar los datos que consume una funcion para optener distintos resultados

**ejemplo**:
*crear una funcion que recibe un valor numero y retorna su raiz cuadrada*
```python
def sqrt(valor):
    return valor**(1/2)
# Nota: es este caso , el valor 4 es un argumento de las funcion 
sqrt(4)
```

Cuando llamamos a una funcion con `argumentos`, los valores de estos argumentos se copian en los correspondiente `parametro` dentro de la funcion
```python
def ejem(a,b,c):
    return a+b+c
ejem(4,5,6)
```
### Argumetos nominales
En esta aproximacion los argumetos no son copiados e3n un orden  especifico si no 
**que se asigna por un nombre a cada parametro**. Ellos nos permite evitar el problema de conoser o recordar cual es el orden de los parametros en la definicion de la funcion.
Para utilizarlo , basta con realisar una asignacion de cada argumento en la propia llamada a la funcion
**ejemplo**
```python
def buid_cpu(familia,num_core,fecuencia):
    printf("""la cpu es de la familia{familia}con{num_core} cores y con una frecuencia de {frecuebcia}
    """)
#haciendo uso de argumetos nominales
buil_cpu(num_core=4,familia="intel",frecuencia=2.7,)
```
### Argumentos posicionales
Los argumentos son copiados en un orden especificos, en este caso debemos conoser o recordar cual es el orden de los parametros.

**Ejemplo**:
```python
def buid_cpu(familia,num_core,fecuencia):
    printf("""la cpu es de la familia{familia}con{num_core} cores y con una frecuencia de {frecuebcia}
    """)
#Haciendo uso de argumentos posicionales
buil_cpu("intel",4,2.7)
```
### Parametros por defecto
Es posible especificar **valores por defecto** en los parametros de la funcion, en el caso de que no se proporcione un valor al argumento en la llamda a la funcion, el parametro correspondiente tomara un valor definido por defecto.

**Ejemplo**:
```python
def alumnos(nom,app,estado="aprobado"):

alumnos("ruth","castillo")
alumnos("anthony","crusez","desaprobado")
```
### Dsempaquetado/Empaquetado de argumentos(tarea)
El concepto de función es básico en prácticamente cualquier lenguaje de programación. Se trata de una estructura que nos permite agrupar código. Persigue dos objetivos claros:

1.-No repetir fragmentos de código en un programa.

2.-Reutilizar el código en distintos escenarios.

Una función viene definida por su nombre, sus parámetros y su valor de retorno. Esta parametrización de las funciones las convierten en una poderosa herramienta ajustable a las circunstancias que tengamos. Al invocarla estaremos solicitando su ejecución y obtendremos unos resultados. [1]

Definir una función
Para definir una función utilizamos la palabra reservada def seguida del nombre [6] de la función. A continuación aparecerán 0 o más parámetros separados por comas (entre paréntesis), finalizando la línea con dos puntos : En la siguiente línea empezaría el cuerpo de la función que puede contener 1 o más sentencias, incluyendo (o no) una sentencia de retorno con el resultado mediante return.


Definición de una función en Python

Advertencia

Prestar especial atención a los dos puntos : porque suelen olvidarse en la definición de la función.

Hagamos una primera función sencilla que no recibe parámetros:
```python

def say_hello():
    print('Hello!')
```
>[!NOTE]

 Nótese la indentación (sangrado) del cuerpo de la función.

Los nombres de las funciones siguen las mismas reglas que las variables y, como norma general, se suelen utilizar verbos en infinitivo para su definición: load_data, store_values, reset_cart, filter_results, block_request, …

Invocar una función
Para invocar (o «llamar») a una función sólo tendremos que escribir su nombre seguido de paréntesis. En el caso de la función sencilla (vista anteriormente) se haría así:
```python

def say_hello():
    print('Hello!')


say_hello()
Hello!
Nota
```

Como era de esperar, al invocar a esta función obtenemos un mensaje por pantalla, fruto de la ejecución del cuerpo de la función.

Cuando queremos invocar a una función dentro de un fichero *.py lo haremos del mismo modo que hemos visto en el intérprete interactivo:
```python

def say_hello():
    print('Hello!')

# Llamada a la función (primer nivel de indentación)
say_hello()
Importante
```

La función debe estar definida antes del punto en el que sea llamada.

Retornar un valor
Las funciones pueden retornar (o «devolver») un valor. Veamos un ejemplo muy sencillo:
```python
def one():
    return 1


one()
1
Importante
```

No confundir return con print(). El valor de retorno de una función nos permite usarlo fuera de su contexto. El hecho de añadir print() al cuerpo de una función es algo «coyuntural» y no modifica el resultado de la lógica interna.

>[!NOTE]

En la sentencia return podemos incluir variables y expresiones, no únicamente literales.

Pero no sólo podemos invocar a la función directamente, también la podemos asignar a variables y utilizarla:
```python

value = one()

print(value)
1
#También la podemos integrar en otras expresiones, por ejemplo en condicionales:

if one() == 1:
    print('It works!')
else:
    print('Something is broken')

It works!
#Si una función no incluye un return de forma explícita, devolverá None de forma implícita:

def empty():
    x = 0
    # return None

print(empty())
None
#Existe la posibilidad de usar la sentencia return «a secas» (que también devuelve None) y hace que «salgamos» inmediatamente de la función:

def quick():
    return


print(quick())
None
```
Advertencia

En general, esto no se considera una buena práctica salvo que sepamos lo que estamos haciendo. Si la función debe devolver None es preferible ser explícito y utilizar return None. Aunque es posible que en ciertos escenarios nos interese dicha aproximación.

Retornando múltiples valores
Una función puede retornar más de un valor. El «secreto» es hacerlo mediante una tupla:
```python
def multiple():
    return 0, 1  # es una tupla!

Veamos qué ocurre si invocamos a esta función:

result = multiple()

result
(0, 1)

type(result)
tuple
Por lo tanto, podremos aplicar el desempaquetado de tuplas sobre el valor retornado por la función:

a, b = multiple()

a
0

b
1
```









## Funciones internas de python (tarea)
¿Cuáles son las funciones de Python más utilizadas?
A pesar de que los programadores y desarrolladores pueden crear funciones personalizadas con Python, el propio lenguaje incluye una serie de funciones predefinidas que aceleran y facilitan su trabajo a la hora de realizar distintos procesos.

Veamos algunas de las funciones más interesantes y utilizadas en este lenguaje de programación.
```python

Funciones list, type y tuple
Tres de las funciones más utilizadas en Python y que debes dominar son list, type y tuple.

List(). #Con esta función se puede crear un listado y aportan un gran nivel de flexibilidad al trabajar con conjuntos de datos.
Type().#Se trata de una función básica de Python que se utiliza principalmente con objetivos de depuración de código.
Tuple().# Permiten crear una lista, pero con dos características diferentes (inmutabilidad, pues sus valores no pueden ser modificados, y rapidez, pues su uso acelera el proceso de cálculo).
Número PI en Python
Para utilizar el número PI en Python, lo que es fundamental a la hora de realizar muchos cálculos complejos o desarrollar algoritmos avanzados, es necesario recurrir a la función math(). Por ejemplo, utilizando la función math.pi() se obtiene el valor de PI en Python (3,1416…).
```

### Funciones de texto

Se trata de una serie de funciones interesantes a la hora de trabajar con texto en Python, siendo las más utilizadas:
```python

Print(). #Una función básica de Python y que también podemos encontrar en la mayoría de lenguajes de programación, y cuyo fin es mostrar en pantalla un valor (texto o valores).
Len(). #Función para contar el número de caracteres de una cadena de entrada y devolver su valor.
Replace(). #Otra función de texto interesante de este lenguaje de programación que permite sustituir caracteres dentro de una cadena.
Str(). #Conocido también como string, es una función que devuelve la representación de cadena de un número (presenta una secuencia inmutable de caracteres Unicode).
Ord(). #Es una función que muestra el valor ASCII de una cadena de un carácter determinado.
Input(). #Es una función que se utiliza para la entrada de datos por parte de un usuario en los programas desarrollados en Python.
Chr(). #Devuelve la cadena correspondiente a un número entero en relación con el código Unicode (por ejemplo, chr(97) devuelve la cadena “a”.
```

### Funciones numéricas
Las funciones que trabajan con números son realmente útiles en cualquier lenguaje de programación, pues ayudan a resolver muchos problemas y cuestiones matemáticas. Dentro de las funciones numéricas destacadas de Python tenemos:
```python
Sum(). #Una función muy interesante que facilita la suma de valores de una lista o tupla en Python (siempre hablando de números como valores).
Min(). #Con esta función se puede hallar el número más pequeño dentro de una lista, tupla o dos o más argumentos.
Max(). #La función contraria a Min() que, en lugar del número más pequeño, devuelve el valor más grande o mayor.
Range(). #Función de Python para generar una sucesión de números enteros de forma personalizada.
Round(). #Cuando se trabaja con números matemáticos es importante disponer de una función capaz de realizar redondeos después de la coma, siendo esta la función de Python que se encarga de este proceso.
Hex (). #Esta función que se incorporó a partir de la versión 3 de Python, convierte un número entero en una cadena hexadecimal con prefijo “0x”.
Abs(). #Al utilizar esta función sobre un número se obtiene su valor absoluto.
Id(). #Se trata de una función nativa que muestra un número entero que es único para cada objeto en memoria.
Bin(). #Convierte un número entero en una cadena binaria incluyendo el prefijo “0b”.
```
## Tipos de Funciones
## Funciones anonimas  (Funciones de lambda)
## Funciones closure
## Funciones callback
## Programacion Funcional
La programacion funcional no requiere 
```python
list=[5,7,8,4,1]
def nim_minimo(1):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo


####averiguar sobre map(),filter(), reduse() 





