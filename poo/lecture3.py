#xrear una clase de alumnos con los atributos que usted crea por conveniente
#luego instanciar a 4 alumnos
#crear claase:
class Alumnos:
    
    def __init__(self,nombre,dni,edad,raza):
        self.nombre=nombre
        self.dni=dni
        self.edad=edad
        self.raza=raza
        

Ronald=Alumnos("Ronald","768956454",20,"negra")
print(Ronald.nombre)

Juan=Alumnos("juan","768956454",20,"negra")
print(Juan.nombre)

Michael=Alumnos("Michael","768956454",20,"negra")
print(Michael.nombre)


