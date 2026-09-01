Numero, binario = 8, "" # indica el numero que se desea convertir a binario
if Numero == 0: print (0) #indicamos que si el numero es 0, el reultado es 0

while Numero > 0: binario, Numero = str(Numero % 2) + binario, Numero // 2 
print(binario)