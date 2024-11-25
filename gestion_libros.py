class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            if len(self.libros_prestados) < self.limite_libros():
                libro.disponible = False
                self.libros_prestados.append(libro)
                print(f"{self.nombre} ha prestado el libro '{libro.titulo}'.")
            else:
                print(
                    f"{self.nombre} ha alcanzado el límite de libros prestados ({self.limite_libros()})."
                )
        else:
            print(f"El libro '{libro.titulo}' no está disponible para préstamo.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro '{libro.titulo}'.")
        else:
            raise LibroNoPrestadoException(
                f"{self.nombre} no tiene el libro '{libro.titulo}' prestado."
            )

    def limite_libros(self):
        raise NotImplementedError("Este método debe ser implementado en subclases.")

    def __str__(self):
        libros = ", ".join([libro.titulo for libro in self.libros_prestados]) or "Ninguno"
        return f"Usuario: {self.nombre}, Libros prestados: {libros}"


class Estudiante(Usuario):
    def limite_libros(self):
        return 3


class Profesor(Usuario):
    def limite_libros(self):
        return 5


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_inventario(self):
        print("Inventario de la biblioteca:")
        for libro in self.libros:
            print(libro)

    def buscar_libro(self, criterio, valor):
        encontrados = [
            libro
            for libro in self.libros
            if getattr(libro, criterio, "").lower() == valor.lower()
        ]
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros con {criterio}: {valor}")


class LibroNoPrestadoException(Exception):
    pass


# Crear algunos libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "123-456")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "789-012")
libro3 = Libro("1984", "George Orwell", "345-678")

# Crear usuarios
estudiante = Estudiante("Juan", "12345")
profesor = Profesor("Dra. Elena", "54321")

# Crear la biblioteca
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Prestar libros
estudiante.prestar_libro(libro1)  # Préstamo exitoso
profesor.prestar_libro(libro2)  # Préstamo exitoso

# Intentar prestar un libro no disponible
estudiante.prestar_libro(libro2)

# Mostrar inventario
biblioteca.mostrar_inventario()

# Devolver libros
profesor.devolver_libro(libro2)  # Devolución exitosa

# Intentar devolver un libro no prestado (lanzará excepción)
try:
    estudiante.devolver_libro(libro3)
except LibroNoPrestadoException as e:
    print(f"Error: {e}")

# Buscar libros por autor
biblioteca.buscar_libro("autor", "George Orwell")


