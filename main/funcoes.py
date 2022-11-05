# from main.main import extrato


def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f'Deposito: R$ {valor:.2f}')
    else:
        print('A operação falhou')
    return saldo, extrato