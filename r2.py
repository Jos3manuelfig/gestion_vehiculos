import re

# . Buscar números en un texto

texto = "Mi número de teléfono es 123-456-7890 y mi código postal es 56789."

codigo_postal = re.findall(r"\d+", texto)
print(codigo_postal)


# Patrón para un número de teléfono en formato 123-456-7890

telefono = "123-456-7890"
pattern = re.findall(r"^\d{3}-\d{3}-\d{4}$", telefono)
print(pattern)
