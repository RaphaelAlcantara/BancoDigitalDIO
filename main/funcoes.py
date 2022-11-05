def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f'Deposito: R$ {valor:.2f}')
    else:
        print('A operação falhou')
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saque, LIMITE_SAQUE):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_limitesaque = numero_saque >= LIMITE_SAQUE

    if excedeu_saldo:
        print('Saldo insuficiente')

    elif excedeu_limite:
        print('Limite excedido')

    elif excedeu_limitesaque:
        print('Limite de saques excedido')

    else:
        saldo -= valor
        extrato.append(f'Saque: R$ {valor:.2f}')

        print('Saque realizado com sucesso')
        numero_saque += 1

    return saldo, extrato, numero_saque
