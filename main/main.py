import funcoes

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair 
=>"""

saldo = 0
limite = 500
extrato = []
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
    if opcao == 'q':
        break
    elif opcao == 'd':
        print('Depositar')
        print("-" * 30)
        valor = float(input('Valor do deposito: '))
        saldo, extrato = funcoes.deposito(saldo, valor, extrato)

    elif opcao == 's':
        print('Sacar')
        print("-" * 30)

        valor = float(input('Valor do saque: '))
        saldo, extrato, numero_saque = funcoes.sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                                                     numero_saque=numero_saque, LIMITE_SAQUE=LIMITE_SAQUE)

    elif opcao == 'e':
        print('Extrato')
        print("-" * 30)
        print('Saldo: R$ ', saldo)
        print("Seus ultimos movimentos: ")
        for movimento in extrato:
            print(f"{movimento}")
    else:
        print('Opção inválida')
