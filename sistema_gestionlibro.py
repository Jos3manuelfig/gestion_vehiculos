from datetime import datetime

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, copias_totales: int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.copias_totales = copias_totales
        self.copias_disponibles = copias_totales

    def mostrar_informacion(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}) - {self.copias_disponibles}/{self.copias_totales} copias disponibles."

class Usuario:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre} ({self.correo}) - Libros prestados: {len(self.libros_prestados)}"

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.historial_prestamos = []

    def agregar_libro(self, titulo: str, autor: str, isbn: str, copias_totales: int):
        if isbn in self.libros:
            print("Este libro ya está registrado en la biblioteca.")
        else:
            nuevo_libro = Libro(titulo, autor, isbn, copias_totales)
            self.libros[isbn] = nuevo_libro
            print(f"Libro '{titulo}' agregado exitosamente.")

    def registrar_usuario(self, nombre: str, correo: str):
        if correo in self.usuarios:
            print("Este usuario ya está registrado.")
        else:
            nuevo_usuario = Usuario(nombre, correo)
            self.usuarios[correo] = nuevo_usuario
            print(f"Usuario '{nombre}' registrado exitosamente.")

    def consultar_libros_disponibles(self):
        print("\nLibros disponibles en la biblioteca:")
        for libro in self.libros.values():
            print(libro.mostrar_informacion())

    def prestar_libro(self, correo: str, isbn: str):
        if correo not in self.usu arios:
            print("Usuario no encontrado.")
            return

        if isbn not in self.libros:
            print("Libro no encontrado.")
            return

        usuario = self.usuarios[correo]
        libro = self.libros[isbn]

        if len(usuario.libros_prestados) >= 3:
            print("El usuario ya tiene el máximo de 3 libros prestados.")
            return

        if libro.copias_disponibles <= 0:
            print("No hay copias disponibles de este libro.")
            return

        # Realizar préstamo
        libro.copias_disponibles -= 1
        usuario.libros_prestados.append((libro, datetime.now()))
        self.historial_prestamos.append((usuario, libro, datetime.now()))
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre} exitosamente.")

    def devolver_libro(self, correo: str, isbn: str):
        if correo not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[correo]
        libro_prestado = next((libro for libro, _ in usuario.libros_prestados if libro.isbn == isbn), None)

        if not libro_prestado:
            print("El usuario no tiene este libro prestado.")
            return

        # Realizar devolución
        libro_prestado.copias_disponibles += 1
        usuario.libros_prestados = [(libro, fecha) for libro, fecha in usuario.libros_prestados if libro.isbn != isbn]
        print(f"Libro '{libro_prestado.titulo}' devuelto exitosamente.")

    def mostrar_historial_prestamos(self):
        print("\nHistorial de préstamos:")
        for usuario, libro, fecha in self.historial_prestamos:
            print(f"{fecha.strftime('%Y-%m-%d %H:%M:%S')} - {usuario.nombre} prestó '{libro.titulo}'.")

# Interfaz de texto para el usuario
def menu_biblioteca():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Menú Biblioteca ---")
        print("1. Agregar libro")
        print("2. Registrar usuario")
        print("3. Consultar libros disponibles")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Mostrar historial de préstamos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            isbn = input("ISBN del libro: ")
            copias = int(input("Número de copias totales: "))
            biblioteca.agregar_libro(titulo, autor, isbn, copias)
        elif opcion == "2":
            nombre = input("Nombre del usuario: ")
            correo = input("Correo del usuario: ")
            biblioteca.registrar_usuario(nombre, correo)
        elif opcion == "3":
            biblioteca.consultar_libros_disponibles()
        elif opcion == "4":
            correo = input("Correo del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(correo, isbn)
        elif opcion == "5":
            correo = input("Correo del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.devolver_libro(correo, isbn)
        elif opcion == "6":
            biblioteca.mostrar_historial_prestamos()
        elif opcion == "7":
            print("Gracias por usar el sistema de la biblioteca. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el sistema
if __name__ == "__main__":
    menu_biblioteca()
