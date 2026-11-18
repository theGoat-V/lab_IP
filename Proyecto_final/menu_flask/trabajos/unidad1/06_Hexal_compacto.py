Numero, hexadecimal = 10, "" # Indica el numero que se desea convertir a hexadecimal
if Numero == 0: print (0) #indicamos que si el numero es 0, el reultado es 0
while Numero >0: # Mientras el numero sea mayor que 0
    residuo = Numero % 16 #Se obtiene el residuo de la division entre el numero y 16
    if residuo == 10: #Si el residuo es 10, se asigna la letra A a la variable hexadecimal
        hexadecimal