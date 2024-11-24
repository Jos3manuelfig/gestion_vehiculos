import re

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$"

clave = "Password2024"

if re.match(pattern, clave):
    print(f"{clave} es  valida")
else:
    print(f"clave invalida")
