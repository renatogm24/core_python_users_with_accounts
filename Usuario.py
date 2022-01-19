from Cuenta import CuentaBancaria

class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email, numCuentas=2):
        self.name = name
        self.email = email
        self.cuentas = []
        for x in range(numCuentas):
          self.cuentas.append(CuentaBancaria(0.02,500))

    # agregando el método de depósito
    def hacer_deposito(self, amount, numero=0):
        self.cuentas[numero].deposito(amount)
        return self
    def hacer_retiro(self, amount,numero=0):
        self.cuentas[numero].retiro(amount)
        return self
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}")
        for i in range(len(self.cuentas)):
          print(f"Cuenta {i+1}: Balance: ${self.cuentas[i].balance}")
        print("----------")
        return self
    def transfer_dinero(self, other_user, amount, numRet=0, numDep=0):
        self.cuentas[numRet].retiro(amount)
        other_user.cuentas[numDep].deposito(amount)
        return self