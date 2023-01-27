menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair


=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do deposito: "))


        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f} \n'

        else:
            print("operação falhou! o valor informado é invalido")

    elif opcao =="s":
        valor = float(input("informe o valor de saque: "))

        exedeu_saldo = valor > saldo

        exedeu_limite = valor > limite

        exedeu_saques = numero_saques >= LIMITE_SAQUES 

        if exedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")
        
        elif exedeu_limite:
            print("Operação falhou! O valor do saque exede o limite.")

        elif exedeu_saques:
            print("Operação falhou! Número máximo de saques exedido.")
        
        elif valor> 0:
            saldo -= valor
            extrato += f'saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print("Operação falhor! O valor informado é invalido.")

    elif opcao == "e":
        print("EXTRATO".center(30,"*"))
        print("Não foram ralizadas movimentações." if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}\n')
        print("*".center(30,"*"))

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")
