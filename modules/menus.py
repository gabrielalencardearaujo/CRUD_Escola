Menu_Secundario = ('\n##### Menu', '(1) Incluir', '(2) Listar', '(3) Editar', '(4) Excluir', '(9) Voltar ao menu principal\n')
Menu_Principal = ('######### MENU PRINCIPAL #########', '', '(1) Gerenciar Estudantes', '(2) Gerenciar Professores','(3) Gerenciar Disciplinas', '(4) Gerenciar Turmas', '(5) Gerenciar Matriculas', '(9) Sair \n')

def menuPrincipal(choice=None):
    """
    Funcao para printar o menu principal e/ou retornar o nome da opcao escolhida de acordo com o valor indicado pelo usuario

    :param choice: Recebe ou nao a opcao escolhida pelo ususario.
    :return: Retorna a opcao escolhida no menu principal.
    """
    if not choice:
        for items in Menu_Principal:
            print(items)
    else:
        for opcoes in Menu_Principal:
            if (opcoes[1:2] == choice):
                return opcoes[14:]

def menu_secundario(name_option):
    for index, value in enumerate(Menu_Secundario):
        if index == 0:
            print(value, name_option, '#####')
        else:
            print(value)