'''
Listas em Python
fatiamento
append, insert, pop, del, clear, extend. +
min, max
range
'''

# #         0    1    2    3    4    5
# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# #        -6   -5   -4   -3   -2   -1
#
# lista[5] = 'Qualquer coisa'
#
# print(lista[-1]) #Mostra o ultimo indice da lista
# print(lista[0:3])#Mostra a lista do indice 0 até o 2 não contando o 3
# print(lista[:3]) #Mostra a lista do indice 0 até o 2 não contando o 3
# print(lista[2:]) #Mostra a lista começando pelo indice dois em diante
# print(lista[::2]) #Mostra o conteudo da lista pulando de 2 em 2
# print(lista[::-1]) #Mostra lista invertida

# # EXTEND (SERVE PARA CONCATERNAR UMA LISTA COM A OUTRA)
# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = l1 + l2
# l1.extend(l2)
#
# print(f'Lista 1: {l1}')
# print(f'Lista 2: {l2}')
# print(f'Lista 3: {l3}')

# # APPEND (Insere um novo valor no final da lista)
# l1 = [1,2,3]
# l2 = [4,5,6]
# l2.append('b')
#
# print(f'Lista 1: {l1}')
# print(f'Lista 2: {l2}')

# # INSERT (Insere um novo valor na lista no indice que vc informar )
# l1 = [1,2,3]
# l2 = [4,5,6]
# l2.insert(0,'banana')
#
# print(f'Lista 1: {l1}')
# print(f'Lista 2: {l2}')

# # POP (Remove o ultimo elemento da lista)
# l1 = [1,2,3]
# print(f'Lista 1: {l1}')
#
# l1.insert(0,'banana')
# print(f'Lista 1: {l1}')
#
# l1.pop()
# print(f'Lista 1: {l1}')

# DEL (Remove o elemento que for informado pelo indice)
# l1 = [1,2,3,4,5,6,7,8,9]
# del(l1[3:5])
# print(f'Lista 1: {l1}')
# l1.insert(0, 'abacate')
# l1.insert(-1,'lua')
# print(f'Lista 1: {l1}')
# del(l1[-1])
# print(f'Lista 1: {l1}')

# # MIN E MAX (Retorna o primeiro e ultimo elemento da lista)
# l1 = [1,2,3,4,5,6,7,8,9]
# print( 'MAX: ', max(l1) )
# print( 'MIN: ', min(l1) )

# # RANGE
# l1 = list(range(1,10))
# print(l1)
#
# l2 = list(range(0,81,8))
# print(l2)

# l2 = [0,1,2,3,4,5,6,7,8,9]
#
# soma = 0
# for valor in l2:
#     soma += valor
#     print(f'{soma} + {valor} = {soma}')
#
# print(soma)
#
# l1 = ['String', True, 10, -20.5]
#
# for elem in l1:
#     print(f'O tipo do elem é {type(elem)} e seu valor é {elem}')


