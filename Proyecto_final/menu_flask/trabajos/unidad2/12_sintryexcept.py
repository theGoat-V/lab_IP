while True:
        edad = int(input("Edad: "))
        if 0 <= edad <= 120:
            break
        print("La edad debe estar entre 0 y 120 años.")
        if type(edad) is not int:
           print("Escribe un numero entero.")

print(f"Edad registrada: {edad}")