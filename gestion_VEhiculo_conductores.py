class Persona:
    def __init__(self, nombre, edad, dni, tipo):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.tipo = tipo

    def mostrar_info(self):
        return f" {self.nombre}, {self.edad} años, DNI: {self.dni}, Tipo: {self.tipo}"


class Conductor(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni, tipo="conductor")
        self.vehiculo = None

    def conducir(self, vehiculo):
        if vehiculo.dispibiliad:
            self.vehiculo = vehiculo  # Asignamos el vehículo al conductor
            vehiculo.asignarconductor(self)
            vehiculo.dispibiliad = False
            print(f"{self.nombre} está conduciendo el vehículo {vehiculo.marca} {vehiculo.modelo}.")
        else:
            print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} no está disponible para conducir.")

    def mostrar_info(self):
        return f"Conductor: {self.nombre}, {self.edad} años, DNI: {self.dni}"


class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje, disponibilidad):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.dispibiliad = disponibilidad
        self.conductor = None  # Añadimos un atributo para guardar al conductor asignado

    def mantenimiento(self):
        if not self.dispibiliad:
            print(f"El vehículo {self.marca} {self.modelo} necesita mantenimiento.")
            self.kilometraje += 500
            self.dispibiliad = True
        else:
            print(f"El vehículo {self.marca} {self.modelo} ya está disponible.")

    def asignarconductor(self, conductor):
        if self.conductor is None:
            self.conductor = conductor
            print(f"El conductor {conductor.nombre} ha sido asignado al vehículo {self.marca} {self.modelo}.")
        else:
            print(f"El vehículo {self.marca} {self.modelo} ya tiene asignado al conductor {self.conductor.nombre}.")

    def mostrar_info(self):
        return f"Vehículo {self.marca} {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje}, Disponible: {self.dispibiliad}"


class Mecanico(Persona):
    def __init__(self, nombre, edad, dni):
        super().__init__(nombre, edad, dni, tipo="mecánico")

    def reparar(self, vehiculo):
        if not vehiculo.dispibiliad:
            print(f"{self.nombre} está reparando el vehículo {vehiculo.marca} {vehiculo.modelo}.")
            vehiculo.mantenimiento()  # El mecánico realiza el mantenimiento.
        else:
            print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} no necesita reparación.")

    def mostrar_info(self):
        return f"Mecánico: {self.nombre}, {self.edad} años, DNI: {self.dni}"


class GestorDeFlota:
    def __init__(self):
        self.vehiculos = []
        self.conductores = []
        self.mecanicos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def agregar_conductor(self, conductor):
        self.conductores.append(conductor)

    def agregar_mecanico(self, mecanico):
        self.mecanicos.append(mecanico)

    def asignar_vehiculo_a_conductor(self, conductor, vehiculo):
        if vehiculo in self.vehiculos and conductor in self.conductores:
            if vehiculo.conductor is None:  # Verificamos si ya hay un conductor asignado
                conductor.conducir(vehiculo)
            else:
                print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} ya está asignado a {vehiculo.conductor.nombre}. No se puede asignar un nuevo conductor.")

    def realizar_mantenimiento(self, vehiculo, mecanico):
        if vehiculo in self.vehiculos and mecanico in self.mecanicos:
            mecanico.reparar(vehiculo)


# Crear instancias de los objetos
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 15000, True)  # Vehículo disponible
vehiculo2 = Vehiculo("Ford", "F-150", 2018, 30000, True)  # Vehículo disponible

conductor1 = Conductor("Carlos", 30, "12345678A")
mecanico1 = Mecanico("José", 45, "87654321B")
conductor2 = Conductor("Chupichupi", 30, "SDSDD")

# Crear el gestor de flota
gestor = GestorDeFlota()
gestor.agregar_vehiculo(vehiculo1)
gestor.agregar_vehiculo(vehiculo2)
gestor.agregar_conductor(conductor1)
gestor.agregar_conductor(conductor2)
gestor.agregar_mecanico(mecanico1)

# Asignar un vehículo a un conductor
gestor.asignar_vehiculo_a_conductor(conductor1, vehiculo1)  # Esto asignará el vehículo al conductor 1
gestor.asignar_vehiculo_a_conductor(conductor2, vehiculo1)  # Esto no podrá asignar el vehículo al conductor 2

# Realizar mantenimiento con un mecánico
gestor.realizar_mantenimiento(vehiculo1, mecanico1)

# Mostrar información
print(vehiculo1.mostrar_info())
print(conductor1.mostrar_info())
print(mecanico1.mostrar_info())
