from dados import produtos, pessoas, lista
from functools import reduce

# # Reduce na Lista
# #Exemplo de como o reduce funciona
# acumula = 0
# for item in lista:
#     acumula += item
#
# print(acumula)
#
# # USANDO REDUCE
# soma_lista = reduce(lambda ac, i: i + ac, lista, 0) # Recebe função, objeto que aplicava a funcao, iniciador no caso 0
# print(soma_lista)

# # REDUCE NOS PRODUTOS
# soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
# print(f'Total produtos: {soma_precos}')
# print(f'Media produtos: {soma_precos / len(produtos)}')

# REDUCE NAS PESSOAS
soma_idade = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)
print(f'Total idades: {soma_idade}')
print(f'Media idades: {soma_idade / len(pessoas)}')
