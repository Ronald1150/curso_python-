class Agencia:
    def __init__(self, nombre, apellido, dni, num_asientos, fecha_viaje):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.num_asientos = num_asientos
        self.fecha_viaje = fecha_viaje
        self.origen = None
        self.destino = None
        self.estado = "Pendiente"

    def set_origen(self, origen):
        self.origen = origen

    def set_destino(self, destino):
        self.destino = destino

    def ingresar(self):
        self.estado = "Ingresado"

    def cancelar(self):
        self.estado = "Cancelado"

    def viaje(self):
        self.estado = "En viaje"

    def ver_estado(self):
        return f"Estado del pasaje: {self.estado}"

# Ejemplo de uso
pasajero = Agencia("Juan", "Pérez", "12345678", 2, "2024-10-15")
pasajero.set_origen("Lima")
pasajero.set_destino("Cusco")
pasajero.ingresar()
print(pasajero.ver_estado())  # Salida: Estado del pasaje: Ingresado
