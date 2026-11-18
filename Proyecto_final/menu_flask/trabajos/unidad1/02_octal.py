Numero = 8
if Numero == 0
print "0"

octal =""
while Numero >0:
    residuo = Numero % 8
    octal = str(residuo) + octal
    Numero = Numero // 8

    print(octal)
    