import json

def saveJSON(escola):
    with open('database/ESCOLA.json', 'w+', encoding="utf-8") as file:
        if escola:
            list_to_json = json.dumps(escola, indent=True)
            file.write(list_to_json)
        else:
            escola = {
                'Estudantes': [
                    {'Codigo do Aluno': 0,
                     'Nome do Aluno': '',
                     'CPF do Aluno': ''
                     },
                ],
                'Professores': [
                    {'Codigo do Professor': 0,
                     'Nome do Professor': '',
                     'CPF do Professor': ''
                     }
                ],
                'Disciplinas': [
                    {'Codigo da Disciplina': 0,
                     'Nome da Disciplina': ''
                     }
                ],
                'Turmas': [
                    {'Codigo da Turma': 0,
                     'Codigo do Professor': 0,
                     'Codigo da Disciplina': 0
                     }
                ],
                'Matriculas': [
                    {'Codigo Matricula': 0,
                     'Codigo da Turma': 0,
                     'Codigo do Estudante': 0
                     }
                ]
            }
            list_to_json = json.dumps(escola, indent=True)
            file.write(list_to_json)
            return escola
