class Persona:
    def __init__(self, nombre, edad, dni, tipo):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.tipo = tipo


    def mostrar_info(self):
        return f" {self.nombre}, {self.edad} años, DNI: {self.dni}, Tipo: {self.tipo}"

class Conductor(Persona):
    def __init__(self, nombre,edad,dni):
        super().__init__(nombre,edad,dni,tipo="conductor")
        self.vehiculo = None

    def conducir(self, vehiculo):
        if vehiculo.disponibilidad:
            self.vehiculo = vehiculo
            vehiculo.asignar_conductor(self)

            print(f"{self.nombre} está conduciendo el vehículo {vehiculo.marca} {vehiculo.modelo}.")
        else:
            print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} no está disponible para conducir.")

    def mostrar_info(self):
        return f" Conductor: {self.nombre}, {self.edad} años,  Dni:{self.dni}"





class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje, disponibilidad):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.disponibilidad = disponibilidad
        self.conductor = None  # Añadimos un atributo para guardar al conductor asignado

    def mantenimientp(self):
        if not self.disponibilidad:
            print(f" Vehiculo {self.modelo} {self.marca} necesita mantenimineto")
            self.kilometraje+=5000
            self.dispibiliad = True
        else:
            print(f" Vehiculo {self.modelo} {self.marca} esta disponible !!!")


    def asignar_conductor(self, conductor):
        if self.conductor is None:
            self.conductor = conductor
            print(f"el conductor {conductor.nombre} ha sido asignado al vehiculo {self.marca} {self.modelo}")
        else:
            print(f"el vehiculo {self.marca} {self.modelo} ya tiene asignado al conductor {self.conductor.nombre}")

    def mostrar_info(self):
        return f"Vehículo {self.marca} {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje}, Disponible: {self.dispibiliad}"