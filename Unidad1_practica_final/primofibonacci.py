n = int(input("Leer número: "))
es_primo = True
if n <= 1:
    es_primo = False
else:
    i = 2
    while i <= n:
        if n % i == 0:
            es_primo == False
            break
        i = i + 1

if es_primo == True:
    print("es primo")
else:
    print("no primo")
if n <= 0:
    a = 0
    b = 1
    while a < n:
        siguiente = a + b
        a = b
        b = siguiente
    if a == n:
        print("Fibonacci")
    if a != n:
        print("No Fibonacci")
