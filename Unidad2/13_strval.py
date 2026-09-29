"""
while True:
    nombre = input("Nombre:").strip()
    print(nombre) #
    if nombre and nombre.replace(" ", "").isalpha():
        print("Nombre")
        break

    print("Usa letras y no dejes el nombre vacio.")

nombre_normalizado = nombre.title()
print(f"Hola, {nombre_normalizado}")
"""

while True:
    nombre = input("Nombre: ").strip()
    nombre = " ".join(nombre.split())  # colapsa espacios múltiples
    if nombre and nombre.replace(" ", "").isalpha():
        break

    print("Usa letras y no dejes el nombre vacio.")

nombre_normalizado = nombre.title()
print(f"Hola, {nombre_normalizado}")