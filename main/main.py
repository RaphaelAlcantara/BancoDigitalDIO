import funcoes
import cad_usuario

# import validador_cpf

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar
[5] Listar
[6] Criar Conta
[7] Listar Contas
[q] Sair 
=>"""

# variaveis globais
LIMITE_SAQUE = 3
AGENCIA = "0001"

saldo = 0
limite = 500
numero_saque = 0

cpf_cadastrado = []
usuario_cadastrado = []
contas = []
extrato = []

while True:
    opcao = input(menu)
    if opcao == 'q':
        break
    elif opcao == '1':
        print('Depositar')
        print("-" * 30)
        valor = float(input('Valor do deposito: '))
        saldo, extrato = funcoes.deposito(saldo, valor, extrato)

    elif opcao == '2':
        print('Sacar')
        print("-" * 30)

        valor = float(input('Valor do saque: '))
        saldo, extrato, numero_saque = funcoes.sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                                                     numero_saque=numero_saque, LIMITE_SAQUE=LIMITE_SAQUE)

    elif opcao == '3':
        print('Extrato')
        print("-" * 30)
        saldo, extrato = funcoes.tirar_extrato(saldo, extrato=extrato)

    elif opcao == '4':
        print('Cadastrar')
        print("-" * 30)
        usuario_cadastrado, cpf_cadastrado = cad_usuario.cadastrar_usuario(usuario_cadastrado, cpf_cadastrado)

    elif opcao == '5':
        print('Listar Cadastrados')
        print("-" * 30)

        for i in cpf_cadastrado:
            print(i)

        cad_usuario.listar_usuario(usuario_cadastrado)

    elif opcao == '6':
        print('Criar Conta')
        print("-" * 30)

        numero_conta = len(contas) + 1
        conta = cad_usuario.criar_conta(AGENCIA, numero_conta, cpf_cadastrado)
        if conta is not None:
            contas.append(conta)

    elif opcao == '7':
        print('Listar Contas')
        print("-" * 30)
        for conta in contas:
            print(conta)
