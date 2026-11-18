Numero = 12 
if Numero == 0:
    print ("0")

letras = "0123456789ABCDEF"

hexadecimal = ""
while Numero > 0:
        residuo = Numero % 16
        hexadecimal = letras[residuo] + hexadecimal
        Numero = Numero // 16
print(hexadecimal)