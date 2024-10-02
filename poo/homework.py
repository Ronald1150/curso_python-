#crear una clase bANCO
#sus atributos sera nombre ,apellidos,dni,numero de cuenta
#y saldo inicial

#como metodos podremos hacer deposito retirar dinero y ver estado de cuenta
class Banco:

    def __init__(self,nombre,apellidos,dni,numero_de_cuenta):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.numero_de_cuenta=numero_de_cuenta


Ronald=Banco("Ronald","valencia_quispe","796566566","9646696546545")
print(Ronald.apellidos)


Juan=Banco("Juan","valencia_quispe","796566565","9646696546544")
print(Juan.dni)

Rosa=Banco("Rosa","valencia_quispe","796566564","9646696546543")
print(Rosa.nombre)

Michael=Banco("MichaEL","valencia_quispe","796566565","9646696546542")
print(Michael.numero_de_cuenta)



#Metodos
def

