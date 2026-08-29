numero = int(input("Leer numero: "))
es_primo = True

if numero <= 1:
    es_primo = False
else:
    i = 2
    while i < numero:
        if numero % i == 0:
            es_primo = False
        i = i + 1

if es_primo == True:
    print("Es primo")

    a = 0
    b = 1
    while a < numero:
        siguiente = a + b
        a = b
        b = siguiente

    if a == numero:
        print("Esta en Fibonacci")
    else:
        print("No esta en Fibonacci")
else:
    print("No es primo")

"""
Gustavo Alonso Navarro Martinez
"""
