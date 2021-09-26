"""
Split, Join, Enumarate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumarate - Enumerar elementos da lista # list / iteraveis
"""

# # SPLIT
#
# string = "O Brasil é o pais do futebol, o Brasil é penta."
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
#
# print(f'Lista 1: {lista_1}')
# print(f'Lista 2: {lista_2}')

# for valor in lista_1:
#     print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')

# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
#
# for valor in lista_2:
#     print(valor.strip().capitalize())

###############

#JOIN
string_2 = 'O Brasil é penta'
lista = string_2.split(' ')
string_3 = ' '.join(lista)

print(string_2)
print(lista)
print(string_3)

# #ENUMERATE
# lista = ['Luiz', 'João', 'Maria']
#
# for indice, nome in enumerate(lista):
#     print(indice, nome)
