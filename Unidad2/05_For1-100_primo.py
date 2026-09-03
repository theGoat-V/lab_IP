"""
for numero in range(1,101,2):
    primo = numero % 2 != 0 or numero != 3 or numero != 5 or numero != 7
    print(numero, primo)
"""
for numero in range(1,101, 2):
    primo= numero % 2 != 0 or numero % 3 != 0 or numero % 5 != 0 or numero % 7 != 0
    print(numero, primo)