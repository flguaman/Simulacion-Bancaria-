class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad} en la cuenta de {self.titular}. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Se han retirado {cantidad} de la cuenta de {self.titular}. Nuevo saldo: {self.saldo}")
            else:
                print("Fondos insuficientes para realizar la operación")
        else:
            print("La cantidad a retirar debe ser mayor que 0")

    def consultar_saldo(self):
        print(f"El saldo de la cuenta de {self.titular} es: {self.saldo}")


def main():
    # Crear una cuenta
    nombre_titular = input("Ingrese el nombre del titular de la cuenta: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    cuenta = CuentaBancaria(nombre_titular, saldo_inicial)

    while True:
        print("\nOpciones:")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Consultar saldo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == "3":
            cuenta.consultar_saldo()
        elif opcion == "4":
            print("Gracias por usar el servicio bancario.")
            break
        else:
            print("Opción no válida, por favor seleccione nuevamente.")

if __name__ == "__main__":
    main()