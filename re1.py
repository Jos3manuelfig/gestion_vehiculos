import re

text = " el precio es de $15 y el descuento es de 20%"
precio = re.findall(r"\$\d+", text)
descuento = re.findall(r"\d+%", text)
print(descuento)
print(precio)
