"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem não importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

print('Combinação')
# Mostra todas as combinações possiveis em grupo de 2 sem repetir (Ordem não importa)
for grupo in combinations(pessoas, 2):
    print(grupo)

print('\nPermutação')
# Mostra todas as combinações possiveis em grupo de 2 repetindo alguns grupos (Ordem importa)
for grupo in permutations(pessoas, 2):
    print(grupo)

print('\nProduto')
# Mostra todas as combinações que existem repetindo os valores no caso com repetição de 2
for grupo in product(pessoas, repeat=2):
    print(grupo)

