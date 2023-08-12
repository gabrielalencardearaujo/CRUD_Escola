from manager_json import writeJSON
from modules import verifyErrors
import copy
def editar(primary, escola):
    encontrado = False
    errors = []
    template = copy.copy(escola[primary][0])

    if len(escola[primary]) > 1:
        print(f'** Editando {primary} ** \n')
        code = int(input('Digite o codigo: '))
        if code == 0:
            errors.append('Código não pode ser zero.')
            return

        for index, item in enumerate(escola[primary]):
            if code in item.values():
                for key in item.keys():
                    if 'Codigo' in key:
                        template[key] = int(input(f'novo {key}: '))
                        code_exist = verifyErrors.verifyValues(primary, escola, template[key])

                        if code_exist[0] and index != code_exist[1]:
                            errors.append('Codigo ja cadastrado!')
                            return

                    elif 'CPF' in key:
                        template[key] = input(f'novo {key}: ')
                        cpf_valido = verifyErrors.validar_cpf(template[key])

                        if not cpf_valido:
                            errors.append('CPF invalido!')
                            return
                    else:
                        template[key] = input(f'novo {key}: ')

                    if primary == 'Turmas' or primary == 'Matriculas':
                        checked_ = verifyErrors.verify_Turmas_Matriculas(escola, key, template[key], primary)
                        if checked_:
                            verifyErrors.errors(checked_)
                            return

                    if len(errors) > 0:
                        for _ in errors:
                            verifyErrors.errors(_)
                    else:
                        encontrado = True
                        item[key] = template[key]

        if encontrado:
            writeJSON.saveJSON(escola)
            return f'Todos o(a)s {primary} foram editados!'
        else:
            return 'Codigo não encontrado!'

    else:
        return f'Não há {primary} para editar!'
