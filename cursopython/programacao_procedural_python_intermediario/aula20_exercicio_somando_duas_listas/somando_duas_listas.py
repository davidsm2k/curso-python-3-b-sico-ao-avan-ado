"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def soma_duas_listas(l1, l2):
    lzip = zip(l1, l2)
    lista_soma = list(lzip)
    lista_soma = [(v1 + v2) for v1, v2 in lista_soma]

    return lista_soma

print(soma_duas_listas(lista_a, lista_b))
