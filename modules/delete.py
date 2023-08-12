from manager_json import writeJSON
def deletar(primary, escola):
    if len(escola[primary]) > 1:
        code = int(input('Digite o código: '))
        for dict in escola[primary]:
            if code in dict.values():
                while True:
                    opcao_excluir = input(f'Tem certeza que deseja excluir? [Y/N]').lower()
                    if opcao_excluir == 'y':
                        escola[primary].remove(dict)
                        print(f'\n{primary} foram excluidos!')
                        writeJSON.saveJSON(escola)
                        break
                    elif opcao_excluir == 'n':
                        continue
                    else:
                        print('Digite Y ou N')
                        continue
    else:
        return f'Não há {primary} para excluir'