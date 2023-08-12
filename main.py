from modules import include, list, verifyErrors, delete, update, menus
from manager_json import readJSON, writeJSON

try:
    escola = readJSON.readFile()
except FileNotFoundError:
    escola = writeJSON.saveJSON(None)

while True:
    try:
        menus.menuPrincipal()
        primary_choice = input('Qual menu deseja acessar?: ')

        if 1 <= int(primary_choice) <= 5:
            name_primary_choice = menus.menuPrincipal(primary_choice)
            while True:
                menus.menu_secundario(name_primary_choice)
                secondary_choice = input('Informe a ação desejada: ')

                if int(secondary_choice) == 1:
                    include.incluir(name_primary_choice, escola)

                elif int(secondary_choice) == 2:
                    msg_listado = list.listar(name_primary_choice, escola)
                    verifyErrors.errors(msg_listado)
                    continue

                elif int(secondary_choice) == 3:

                    msg_editado = update.editar(name_primary_choice, escola)
                    verifyErrors.errors(msg_editado)
                    continue

                elif int(secondary_choice) == 4:

                    msg_deletado = delete.deletar(name_primary_choice, escola)
                    verifyErrors.errors(msg_deletado)
                    continue

                elif int(secondary_choice) == 9:
                    break
                else:
                    verifyErrors.errors('Digite uma das opcões acima.')
                    continue
        elif primary_choice == '9':
            print('Finalizando aplicação...')
            break
        else:
            verifyErrors.errors('Digite uma das opções indicadas')
            continue
    except Exception as Error:
        verifyErrors.errors('Digite uma opção correta!', Error)
    except:
        verifyErrors.errors('Algo inesperado aconteceu aqui. 1')
