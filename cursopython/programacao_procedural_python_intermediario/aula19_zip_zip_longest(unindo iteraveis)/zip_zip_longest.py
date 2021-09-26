"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

# #Zip (Une as lista com base na lista menor)
# Cria um iterador
# variavel = zip('Alo', 'Alo')
# print(list(variavel))
#
# variavel = ((x, y) for x, y in zip('Alo', 'Alo'))
# print(list(variavel))
#
# cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
# estados = ['SP', 'MG', 'BA']
#
#
# cidades_estados = zip(estados, cidades) # É um iterador
#
# for valor in cidades_estados:
#     print(valor)

#Zip_longest(Une as lista com base na lista maior e atribui o valor vazio aos campos que tem a mais)
from itertools import zip_longest, count

# cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
# estados = ['SP', 'MG', 'BA']
#
#
# # cidades_estados = zip_longest(estados, cidades) # É um iterador sem valor padrão para campo vazio
# cidades_estados = zip_longest(estados, cidades, fillvalue='Estado') # É um iterador com valor padrão para campo vazio
# print(list(cidades_estados)) # Convertendo gerador em lista e imprimindo valor

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip( # Não utilizamos o zip_longest para ele junto com a def cont() cria um loop infinito
    indice,
    estados,
    cidades
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
