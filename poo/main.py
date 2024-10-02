#nombre de mi clase
class Mascota:
#atributos de mi clase
    nombre="leon"
    edad="5 años"
    sexo="macho"
    raza="chihuahua"
#metodos de mi clase
    def ladrar(self):
        print("guau guau")
        
#instanciar una clase
labrador=Mascota()
labrador.nombre="boby"
print(labrador.nombre)
aleman=Mascota()
aleman.nombre="peruano"
print(aleman.nombre)
