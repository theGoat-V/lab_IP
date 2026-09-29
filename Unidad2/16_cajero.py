def consultar_saldo(saldo):
    print("Saldo: $0.00 ")
def depositar():
    print("Deposito realizado")
def retirar():
    print("Retiro realizado")
def salir():
    print("Saliendo del cajero automatico...")

def mostrar_menu():
    print("Bienvenido al cajero automatico")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    return input("Opcion: ").strip()

def main():
    while True: 
      opcion = input("Opcion: ").strip
      if opcion == "1":
        consultar_saldo()
      elif opcion == "2":
        depositar()
      elif opcion == "3":
        retirar()
      elif opcion == "4":
        salir()
        break
    else:
        print("Opcion invalida")
    main()