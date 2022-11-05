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
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Saldo insuficiente')

        elif excedeu_limite:
            print('Limite excedido')

        elif excedeu_limite_saque:
            print('Limite de saques excedido')

        else:
            saldo -= valor
            extrato.append(f'Saque: R$ {valor:.2f}')
            numero_saque += 1
            print('Saque realizado com sucesso')

    elif opcao == 'e':
        print('Extrato')
        print("-" * 30)
        print('Saldo: R$ ', saldo)
        print("Seus ultimos movimentos: ")
        for movimento in extrato:
            print(f"{movimento}")
    else:
        print('Opção inválida')
