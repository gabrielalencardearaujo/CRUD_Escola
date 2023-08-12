def listar(primary, escola):
    if len(escola[primary]) > 1:
        print(f'** Listando {primary} **')
        for index, value in enumerate(escola[primary]):
            if index != 0:
                print(f'\n {index}: ')
                for chave, valor in value.items():
                    print(' '*3 + f'{chave}: {valor}')
    else:
        return f'Não há {primary} cadastrados.'