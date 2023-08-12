from modules import verifyErrors
from manager_json import writeJSON
import copy
def incluir(primary, escola):
    try:
        template = copy.copy(escola[primary][0])
        erros = []
        for chave,valor in escola[primary][0].items():
            if 'Codigo' in chave:
                template[chave] = int(input(f'{chave}: '))
                checked = verifyErrors.checar_duplicidade(template[chave], primary, escola)
                if checked:
                    erros.append(f'Codigo já Cadastrado!')
                    break
            else:
                template[chave] = input(f'{chave}: ')

            if primary == 'Turmas' or primary == 'Matriculas':
                checked_ = verifyErrors.verify_Turmas_Matriculas(escola, chave, template[chave], primary)
                if checked_:
                    verifyErrors.errors(checked_)
                    return

            if 'CPF' in chave:
                cpf_valido = verifyErrors.validar_cpf(template[chave])
                if not cpf_valido:
                    erros.append('CPF inválido! Digite seu CPF corretamente sem pontos ou hífen')

            if 'Codigo' in chave and template[chave] == 0:
                erros.append('O codigo nao pode ser zero.')

        if len(erros) > 0:
            for value in erros:
                verifyErrors.errors(value)
            return
        else:
            print(f'\n {primary} incluido(s)!')
            escola[primary].append(template)
            writeJSON.saveJSON(escola)

    except Exception as e:
        print(e)
