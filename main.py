from Usuario import Usuario

user1 = Usuario("Renato","abc@test.com",3)
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

user1.transfer_dinero(user3,200,1).mostrar_balance_usuario()
user2.mostrar_balance_usuario()
user3.mostrar_balance_usuario()