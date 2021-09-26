"""
-> É uma lista de listas de numeros inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém numeros entre 1 a 10 e eles podem ser duplicados

Exercicio

-> Crie uma função que encontra o primeiro duplicado considerando o segundo número como a duplicação.
    Requisitos:
        A ordem do numero duplicado é considerada a partir da segunda ocorrencia (o numero duplicado em si).
        Exemplo:
            [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
            [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 5, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
]

def encontra_duplicado(lista):
    duplicado = -1
    lista_aux_inteiros = []

    for item in lista:
        if item in lista_aux_inteiros:
            duplicado = item
            break
        lista_aux_inteiros.append(item)
    return duplicado

for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(lista_de_inteiros, encontra_duplicado(lista_de_inteiros))
