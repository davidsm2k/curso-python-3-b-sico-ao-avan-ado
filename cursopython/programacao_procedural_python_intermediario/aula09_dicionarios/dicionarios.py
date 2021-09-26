## Criando dicionarios
# d1 = {'chave1': 'Valor da chave'}
# print(d1)
#
# d1['nova_chave'] = 'valor da nova chave' # Adicionando nova chave
# print(d1)
#
# print(d1['chave1'])

## Outra forma de criar dicionario
# d2 = dict(chave1 = 'valor da chave', chave2 = 'valor da outra chave')
# d2['nova_chave'] = 'valor da nova chave' # Adicionando nova chave
# print(d2)

# # Chaves com mesmo nome
# d3 = {'chave': 'Valor da chave', 'chave': 'valor da outra chave', 'chave': 'valor real da chave'}
# print(d3)

# d4 = {1: 'Valor da chave', 2: 'valor da outra chave', 3: 'valor real da chave'}
# print(d4)

# Podem ser usados como chaves todos os que são imutaveis
#
# d5 = {
#     'str': 'strings',
#     123: 'numeros',
#     (1,2,3,4): 'Tuplas',
# }

# # Adicionar coisas no dicionario
# d6 = {
#     'str': 'strings',
#     123: 'numeros',
#     (1,2,3,4): 'Tuplas',
# }
#
# d6['novachave'] = 'valor da nova chave'
# d6.update(chaveupdate = 'valor chave update')
#
# print(d6)

# # Para puxar valor do dicionario
# d7 = {
#     'str': 'strings',
#     123: 'numeros',
#     (1,2,3,4): 'Tuplas',
# }
#
# print(d7[(1,2,3,4)])
# print(d7.get('str'))

# # Para apagar/deletar um item do dicionario
# d8 = {
#     'str': 'strings',
#     123: 'numeros',
#     (1,2,3,4): 'Tuplas',
# }
#
# d8.popitem() # Apaga o ultimo item indenpendente de qual seja
# del d8['str']
# d8.pop(123)
# print(d8)

# # Checando valores do dicionario
# d9 = {
#     'str': 'strings',
#     123: 'numeros',
#     (1,2,3,4): 'Tuplas',
# }
#
# print('str' in d9)
# print('str' in d9.keys()) # Olhando se existe 'str' entre as keys
# print('valor' in d9.values()) # Olhando se existe 'valor' entre os valores

# # Usando Dicionario com For
# d10 = {
#     'chave1': 'strings',
#     'chave2': 'numeros',
#     'chave3': 'Tuplas',
# }
#
# print('vendo as chaves')
# for k in d10:
#     print(k)
#
# print('\nvendo os valores')
# for v in d10.values():
#     print(v)
#
# print('\nvendo as chaves e os valores')
# for k in d10.items():
#     print(k)
#
# print('\nCom desempacotamento')
# for k, v in d10.items():
#     print(k, v)

# # Dicionario dentro de dicionario
#
# clientes = {
#     'cliente1': {
#         'nome': 'David',
#         'sobrenome': 'Santos',
#     },
#     'cliente2': {
#         'nome': 'Rafa',
#         'sobrenome': 'Portugal',
#     }
# }
#
# for cliente_k, cliente_v in clientes.items():
#     print(f'Exibindo {cliente_k}')
#     for dados_k, dados_v in cliente_v.items():
#         print(f'\t{dados_k} = {dados_v}')

# # Copiando dicionario
# d11 = {1: 'a', 2: 'b', 3: 'c'}
# v1 = d11 # Aqui o 'v1' e o 'd11' apontam para o mesmo lugar sendo os dois uma coisa só
# v1[1] = 'Luiz' # isso ira modificar tanto o 'v1' como o 'd11'
# print(v1)
# print(d11)
#
# # Copiando de forma raza
# d12 = {1: 'a', 2: 'b', 3: 'c', 4: ['David', 'Santos']}
# v2 = d12.copy() # Faz uma copia raza deixando que vc altere dicionario segundario nas duas versoes da lista
# v2[1] = 'David'
# v2[4][0] = 'Dave'
# print(d12)
# print(v2)
#
# # Copiando de forma definitiva
# import copy
#
# d13 = {1: 'a', 2: 'b', 3: 'c', 4: ['David', 'Santos']}
# v3 = copy.deepcopy(d13) # copiando de forma definitiva usando a biblioteca copy
# v3[1] = 'David'
# v3[4][0] = 'Dave'
# print(d13)
# print(v3)

# # Convertendo listas e tuplas em dicionarios (Somente se tiverem chaves e valores)
# lista = [
#    ['c1', 1],
#    ['c2', 2],
#    ['c3', 3],
# ]
#
# d14 = dict(lista)
#
# print(d14)
#
# tupla = (
#    ('c1', 1),
#    ('c2', 2),
#    ('c3', 3),
# )
#
# d15 = dict(tupla)
#
# print(d15)

# Concatenar dicionarios
d1 = {
    1: 2,
    3: 4,
    5: 6,
}

d2 = {
    'a': 'b',
    'c': 'd',
}
print(d1)
print(d2)
d1.update(d2)
print(d1)
