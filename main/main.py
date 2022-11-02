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

        valor = float(input('Valor do deposito: '))
        if valor > 0:
            saldo += valor
            extrato.append(f'Deposito: R$ {valor}')
        else:
            print('A operação falhou')

    elif opcao == 's':
        print('Sacar')
    elif opcao == 'e':
        print('Extrato')
        print("-" * 30)
        print('Saldo: R$ ', saldo)
        print("Seus ultimos movimentos: ")
        for movimento in extrato:
            print(f"{movimento}")
    else:
        print('Opção inválida')
