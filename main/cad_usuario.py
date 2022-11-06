import validador_cpf


# cadastra usuario


def cadastrar_usuario(usuario_cadastrado, cpf_cadastrado):
    usuario = []

    while True:
        cpf = input('Digite seu CPF: ')
        cpf = validador_cpf.valida_cpf(cpf)
        if not cpf:
            if cpf in cpf_cadastrado:
                print('CPF já cadastrado')
            print('CPF invalido')
            continue
        else:
            cpf_cadastrado.append(cpf)
            usuario.append(cpf)
            print('CPF cadastrado com sucesso')
            break

    nome = input('Digite o nome: ')
    data_nascimento = data()
    endereco = input('Digite a rua - nro - Bairro - Cidade - Estado')
    usuario.append({'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco})

    usuario_cadastrado.append(usuario)

    print('Usuário cadastrado com sucesso')
    return usuario_cadastrado, cpf_cadastrado


# lista usuario
def listar_usuario(usuario_cadastrado):
    for usuario in usuario_cadastrado:
        print(usuario)


def data():
    print('Digite a data de nascimento')
    day = int(input('Insira o dia: '))
    month = int(input('Insira o mês: '))
    year = int(input('Insira o Ano: '))

    data_nsc = "{}/{}/{}".format(day, month, year)
    return data_nsc


def criar_conta(agencia, numero_conta, cpf_cadastrado):
    cpf = input('Digite seu CPF: ')
    cpf = validador_cpf.valida_cpf(cpf)
    if not cpf_cadastrado:
        print('Não há usuários cadastrados')
        return None
    while True:
        if cpf in cpf_cadastrado:
            conta = {'agencia': agencia, 'numero_conta': numero_conta, 'cpf': cpf}
            print('Conta criada com sucesso')
            return conta
        else:
            print('CPF não cadastrado')
            return None


