import re


num_telefono = input("introduzca un numero de telefono  en este formato 122-456-7895:")

pattern = r"^\d{3}-\d{3}-\d{4}$"


if re.match(pattern, num_telefono):
    print(f"El numero {num_telefono} es Valido.")
else:
    print(f"El numero {num_telefono}  ingresado NO es Valido.")
