class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuentas = [CuentaBancaria(),CuentaBancaria()]
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

class CuentaBancaria:
    todas_cuentas = []
    def __init__(self, tasa_interes=0.02, balance = 0):
      self.tasa_interes = tasa_interes
      self.balance = balance
      CuentaBancaria.todas_cuentas.append(self)

    def deposito(self, amount):
      self.balance += amount
      return self
        
    def retiro(self, amount):
      if (CuentaBancaria.puede_retirar(self.balance,amount)):
        self.balance -= amount
      else:
        print("Fondos insuficientes: cobrando una tarifa de $5")
        self.balance -= 5
      return self

    def mostrar_info_cuenta(self):
      print(f"Balance: ${self.balance}")
      return self
        
    def generar_interes(self):
      if (CuentaBancaria.puede_generar_interes(self.balance)):
        self.balance *= (1+self.tasa_interes)
      return self

    @classmethod
    def imprimir_todas_cuentas(cls):
      for cuenta in cls.todas_cuentas:
        cuenta.mostrar_info_cuenta()
    
    @staticmethod
    def puede_retirar(balance,amount):
      if(balance - amount >= 0):
        return True
      else:
        return False

    @staticmethod
    def puede_generar_interes(balance):
      if(balance > 0):
        return True
      else:
        return False


user1 = Usuario("Renato","abc@test.com")
user2 = Usuario("Paco","abc@test.com")
user3 = Usuario("Vanessa","abc@test.com")

user1.hacer_deposito(500,0).hacer_deposito(300,0).hacer_deposito(200,0).hacer_retiro(400,0).mostrar_balance_usuario()
user2.mostrar_balance_usuario()
user3.mostrar_balance_usuario()

print("---------------------")

user1.mostrar_balance_usuario()
user2.hacer_deposito(500).hacer_deposito(300).hacer_retiro(200).hacer_retiro(400).mostrar_balance_usuario()
user3.mostrar_balance_usuario()

print("---------------------")

user1.mostrar_balance_usuario()
user2.mostrar_balance_usuario()
user3.hacer_deposito(1500).hacer_retiro(300).hacer_retiro(200).hacer_retiro(400).mostrar_balance_usuario()

print("---------------------")

user1.transfer_dinero(user3,200).mostrar_balance_usuario()
user2.mostrar_balance_usuario()
user3.mostrar_balance_usuario()