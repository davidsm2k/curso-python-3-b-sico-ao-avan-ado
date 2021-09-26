"""
Desempacotamento de listas em Python
"""
# # EXEMPLO 1
# lista = ['Luiz', 'João', 'Maria']
#
# n1, n2, n3 = lista
#
# print(n1, n2, n3)

# # EXEMPLO 2
# lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
# n1, n2, n3, *outra_lista = lista
#
# print(n1, n2, outra_lista)

# # EXEMPLO 3
# lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
# n1, n2, n3, *outra_lista, ultimo_da_lista = lista
#
# print(ultimo_da_lista)

# # EXEMPLO 4
# lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
# *outra_lista, n1, n2, n3 = lista
#
# print(outra_lista, n2)

# EXEMPLO 5
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
n1,n2, *_ = lista # *_ serve para informar para outros devs que vc não ira usar o resto da lista

print(n1, n2)