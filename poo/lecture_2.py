class Personaje:
    #atributos
    def __init__(self,nombre,edad,usuario,bando,raza):
        self.nombre=nombre
        self.edad=edad
        self.usuario=usuario
        self.bando=bando
        self.raza=raza
    
    def mostrar_personaje(self):
        return{
            "nombre":self.nombre,
            "edad":self.edad,
            "usuario":self.usuario,
            "bando":self.bando,
            "raza":self.raza
            
        }
        


luffy=Personaje("Luffy",18,"gomu gomu no mi","pirata","humano")
print(luffy.nombre)

coby=Personaje("coby",15,"no","sword","humano")
print(coby.bando)

king=Personaje("king",40,"zoan mitologia","pirata","lunaria")
print(king.raza)