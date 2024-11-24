import re

#  (re. match) buca un patron al comizndo de la cadena

result = re.match(r"hola", "hola mundo")
print(result)  # Coincide porque "hola" está al inicio


# (re.search) busca la cadena en cualquier lugar
result = re.search(r"mundo", "hola mundo")
print(result)  # Encuentra "mundo" en cualquier parte de la cadena

# (re.findall) Encuentra todas las coincidencias del patrón en la cadena y las devuelve como una lista.

result = re.findall(r"\d+", "123 abc 456")
print(result)  # ['123', '456']


# (re.finditer) ncuentra todas las coincidencias y devuelve un iterador con objetos Match.
result = re.finditer(r"\d+", "123 abc 456")
for match in result:
    print(match.group())  # 123, 456
