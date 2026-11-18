Numero = 8
if Numero == 0
print "0"

binario =""
while Numero > 0:
    residuo = Numero % 2
    binario = str(residuo) + binario
    Numero = Numero // 2

print(binario)
    