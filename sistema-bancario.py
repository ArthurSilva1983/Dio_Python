# Sistema Bancário

from time import sleep
from datetime import datetime
flag = False
saldo = 0
dep = 0
saq = 0
data = None
EXTRATO = []
LIMITE_SAQUE = 3
saque_atual = 0
o = None
o_ver = '12345'
print("\nBem vindo!\n")
sleep(2)
print(" Sistema Bancário ".center(30, '#'))
print()
while o != 5:
    print(" Opções ".center(20, '='))
    print(" [1] Depósito\n [2] Saque\n [3] Extrato\n [4] Saldo Atual\n [5] Encerrar Programa")
    o = input('Opção: ')
    while o not in o_ver:
        print("Por favor insira uma opção válida!")
        o = input('Opção: ')
    o = int(o)
    match o:
        case 1:
            flag = False
            print("Insira o valor desejado para depósito:")
            while flag is False:
                try:
                    dep = float(input('Depósito: '))
                    if dep <= 0:
                        print("Por favor insira um valor válido!")
                    if type(dep) == float and dep > 0:
                        flag = True
                except ValueError:
                    print("Por favor insira um valor válido!")
            saldo += dep
            data = datetime.today().strftime('%d/%M/%Y, %H:%M:%S')
            EXTRATO.append([data, "Depósito", f"R${dep:.2f}"])
            print("Depósito realizado com sucesso!\n")
        case 2:
            if saque_atual < LIMITE_SAQUE:
                flag = False
                print(f"Saldo Atual: R${saldo:.2f}")
                print("Insira o valor desejado para o saque: ")
                while flag is False:
                    try:
                        saq = float(input('Saque: '))
                        if saq <= 0:
                            print("Por favor insira um valor válido!")
                        if saq > 500:
                            print("O limite por saque é de R$500,00")
                        if type(saq) == float and 0 < saq < 501:
                            flag = True
                    except ValueError:
                        print("Por favor insira um valor válido!")
                if saq > saldo:
                    print("Você não possui saldo suficiente para essa operação!\n")
                else:
                    saldo -= saq
                    saque_atual += 1
                    data = datetime.today().strftime('%d/%M/%Y, %H:%M:%S')
                    EXTRATO.append([data, "Saque", f"R${saq:.2f}"])
                    print("Saque realizado com sucesso!\n")
            else:
                print("Você já atingiu seu limite de saque diário!\n")
        case 3:
            print("Gerando extrato...")
            if EXTRATO:
                sleep(2)
                print(" EXTRATO ".center(15, '='))
                for i in EXTRATO:
                    print(i)
                print(f"Saldo Atual: R${saldo:.2f}\n")
            else:
                print("Não foram realizadas movimentações.\n")
        case 4:
            print(" SALDO ATUAL ".center(20, '='))
            print(f"R${saldo:.2f}\n")
        case 5:
            print("Encerrando...")
            sleep(1)
            break
print("Volte Sempre!")