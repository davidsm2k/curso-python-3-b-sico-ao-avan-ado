from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'José', 'nota': 'B'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamentos, valores_agrupados in alunos_agrupados:
    lista_valores_agrupador = list(valores_agrupados)

    print(f'Agrupamento: {agrupamentos}')
    quantidade = len(lista_valores_agrupador)
    print(f'{quantidade} alunos tiraram nota {agrupamentos}')

    print("Alunos: ")
    for alunos in lista_valores_agrupador:
        print(f'\t{alunos["nome"]}')

    print()
