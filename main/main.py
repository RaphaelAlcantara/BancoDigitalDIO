import funcoes
import cad_usuario

# import validador_cpf

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar
[5] Criar Conta
[q] Sair 
=>"""


# variaveis globais
cpf_cadastrado = []
usuario_cadastrado = []
contas = []
n_conta = 1
saldo = 0
limite = 500
extrato = []
numero_saque = 0
LIMITE_SAQUE = 3

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

        opcao = input("[1] Cadastrar\n[2] Listar\n=>")

        if opcao == '1':
            usuario_cadastrado, cpf_cadastrado = cad_usuario.cadastrar_usuario(usuario_cadastrado, cpf_cadastrado)

        elif opcao == '2':
            cad_usuario.listar_usuario(usuario_cadastrado)


