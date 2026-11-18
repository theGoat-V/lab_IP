edad = 19
tiene_credencial = True 
tiene_adeudo = False 

es_mayor = edad >= 18
documento_valido = tiene_credencial
sin_adeudo = not tiene_adeudo

autorizado = es_mayor and documento_valido and sin_adeudo
print(autorizado)