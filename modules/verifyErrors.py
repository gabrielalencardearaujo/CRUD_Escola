# Funcao abaixo feita pelo chatGPT:
def validar_cpf(cpf):
    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Verificar o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11 % 10
    if digito1 != int(cpf[9]):
        return False

    # Verificar o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11 % 10
    if digito2 != int(cpf[10]):
        return False

    # CPF válido
    return True

def checar_duplicidade(value1, primary, escola):
    for items in escola[primary]:
        if value1 == next(iter(items.values())):
            return True
    return False

def errors(*args):
    for erro in args:
        if erro:
            print(f'\n-> {erro}\n')

def verifyValues(primary, escola, valor):
    for index, item in enumerate(escola[primary]):
        if valor in item.values():
            return True, index
    return False, 0

def verify_Turmas_Matriculas(escola, option, valor, primary):
    if 'Professor' in option and not checar_duplicidade(valor, 'Professores', escola):
        return f'{option} nao encontrado.'
    elif 'Disciplina' in option and not checar_duplicidade(valor, 'Disciplinas', escola):
        return f'{option} nao encontrado.'
    elif 'Turma' in option and not checar_duplicidade(valor, 'Turmas', escola) and not primary == 'Turmas':
        return f'{option} nao encontrado.'
    elif 'Estudante' in option and not checar_duplicidade(valor, 'Estudantes', escola):
        return f'{option} nao encontrado.'

    return False
