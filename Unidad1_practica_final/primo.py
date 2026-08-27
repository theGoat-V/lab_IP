n = int(input("Introduce un número: "))
if n <= 1:
    print("no primo")
i = 2
while i <=n: 
    if n%i == 0 and i != 2:
        print("primo")
        break
    elif n % i == 0 and i == n:
        print("primo")
        break
    elif n % i != 0 and i < n:
        print("no primo")
        break
    i=i+1

