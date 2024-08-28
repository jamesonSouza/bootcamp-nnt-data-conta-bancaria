menu = "[D] Depositar\n[S] Sacar\n[E] Extrato\n[Q] Sair\nO que deseja fazer: "


saldo = 0
extrato=""
numero_saque=0
saque_restante=3
VALOR_MAXIMO_SAQUE = 500
LIMITE_SAQUES = 3

#função de deposito bancario
def depositar(valor,extrato):
    global saldo
    
    if valor > 0:
          saldo += valor
          extrato += f"Depositado: R$ {valor:.2f}\n"

    else:
          print("Operação não realizada: Valor inválido")
    return extrato

#funcão de saque
def sacar(valor, extrato):
    global saldo
    global LIMITE_SAQUES
    global VALOR_MAXIMO_SAQUE
    global numero_saque
    global saque_restante
    sem_saldo =valor > saldo
    sem_limite = valor > VALOR_MAXIMO_SAQUE
    sem_saques_disponiveis =  numero_saque >= LIMITE_SAQUES

    if sem_saldo:
         print("Operação não realizada: Saldo insuficiente")
    
    elif sem_limite:
         print("Operação não realizada: Valor excedido por saque")
    
    elif sem_saques_disponiveis:
         print("Operação não realizada: Limite de saques excedido")
    
    elif valor > 0:
         saldo -=valor
         extrato +=f"Realizado saque de: R$ {valor:.2f}\n"
         numero_saque +=1
         saque_restante -= 1
    
    else:
         print("Operação não realizada: Valor inválido")
    
    return extrato


#funcão de extrato bancario
def exibir_extrato( saldo):
    global extrato
    global numero_saque
    print("***************EXTRATO*****************")

    if extrato=="":            
        print("Não foram realizados transações.")
        print(f"\nSaldo em conta: R$ {saldo:.2f}")
        print(f"\nSaques restantes: {saque_restante}\n")
        print("***************************************")
    else:
        print(extrato)
        print(f"\nSaldo em conta: R$ {saldo:.2f}")
        print(f"\nSaques restantes: {saque_restante}\n\b")
        print("***************************************")

#loop do menu 
while True:
        op = input(menu)

        if op.upper() == "D":
                try:
                    valor = float(input("Digite o valor a ser depositado: R$ "))
                    extrato =depositar(valor,extrato=extrato)
                except ValueError:
                     print("Erro invalido valor")
                
        
        elif op.upper()  == "S":
             valor = float(input("Digite o valor a ser sacado: R$ "))
             
             extrato = sacar(valor=valor, extrato=extrato)

        elif op.upper()  == "E":
              exibir_extrato(saldo=saldo)

        elif op.upper()  == "Q":
              print("Obrigado por usar nosso sistema, até mais.\n")
              break
        
        else:
             print("Opção incorreta tente novamente.\n\n")
              





        